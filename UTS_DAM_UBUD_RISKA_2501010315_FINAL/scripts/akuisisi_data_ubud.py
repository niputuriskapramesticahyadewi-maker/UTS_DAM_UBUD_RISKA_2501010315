"""Akuisisi data tambahan untuk proyek UTS DAM Akomodasi Ubud.

Sumber:
- BPS CSV lokal: dataset dasar hasil ekstraksi publikasi BPS.
- OpenStreetMap Overpass API: data titik/objek akomodasi, JSON mentah disimpan.
- Open-Meteo Historical API: cuaca harian Januari 2025, JSON mentah disimpan.
- Bali Hotels Association: scraping HTML hanya jika robots.txt dapat dibaca dan mengizinkan.
"""
from __future__ import annotations

import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
RAW = BASE_DIR / "data" / "raw"
INTERIM = BASE_DIR / "data" / "interim"
PROCESSED = BASE_DIR / "data" / "processed"
META = BASE_DIR / "metadata"
for folder in (RAW, INTERIM, PROCESSED, META):
    folder.mkdir(parents=True, exist_ok=True)

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "UTS-DAM-Ubud-Student-Project/1.0 (academic research; respectful rate)"
})
TIMEOUT = 45


def save_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def check_robots_and_scrape_bha() -> dict:
    """Scrape directory page only when robots.txt is reachable and permits it."""
    page_url = "https://www.balihotelsassociation.com/our-hotel-and-resorts/?location=ubud"
    robots_url = urljoin(page_url, "/robots.txt")
    result = {
        "source": "Bali Hotels Association",
        "page_url": page_url,
        "robots_url": robots_url,
        "status": "NOT_RUN",
        "http_status": None,
        "robots_http_status": None,
        "records": 0,
        "reason": ""
    }
    try:
        robots_response = SESSION.get(robots_url, timeout=TIMEOUT)
        result["robots_http_status"] = robots_response.status_code
        if not robots_response.ok:
            result["status"] = "NOT_SCRAPED_ROBOTS_UNAVAILABLE"
            result["reason"] = (
                f"robots.txt returned HTTP {robots_response.status_code}; "
                "scraping was not attempted."
            )
            return result

        parser = RobotFileParser()
        parser.set_url(robots_url)
        parser.parse(robots_response.text.splitlines())
        if not parser.can_fetch(SESSION.headers["User-Agent"], page_url):
            result["status"] = "BLOCKED_BY_ROBOTS"
            result["reason"] = "robots.txt does not permit this page."
            return result

        response = SESSION.get(page_url, timeout=TIMEOUT)
        result["http_status"] = response.status_code
        response.raise_for_status()
        (RAW / "bali_hotels_association_ubud.html").write_text(
            response.text, encoding="utf-8"
        )

        soup = BeautifulSoup(response.text, "html.parser")
        records = []
        # Halaman BHA menampilkan kartu properti pada elemen .hotel-item.
        # Ambil nama, area, rating bintang, website, dan lokasi dari kartu tersebut.
        for card in soup.select(".hotel-item"):
            heading = card.select_one(".hotel-item-header h6")
            if not heading:
                continue
            name = " ".join(heading.get_text(" ", strip=True).split())
            area_el = card.select_one(".hotel-item-header .area-name")
            area = " ".join(area_el.get_text(" ", strip=True).split()) if area_el else ""
            # Pastikan hasil benar-benar milik area Ubud, bukan menu navigasi atau hotel Bali lain.
            if area.strip().casefold() != "ubud":
                continue
            website_link = None
            for link in card.select(".hotel-item-reservation a[href]"):
                href = link.get("href", "")
                if href.startswith("http") and "google.com/maps" not in href and "wa.me/" not in href:
                    if "facebook.com" not in href and "instagram.com" not in href:
                        website_link = href
                        break
            location_link = next(
                (link.get("href", "") for link in card.select(".hotel-item-reservation a[href]")
                 if "google.com/maps" in link.get("href", "")),
                ""
            )
            rating = len(card.select(".hotel-rate .imoon-star"))
            price_el = card.select_one(".hotel-item-price .price")
            price = " ".join(price_el.get_text(" ", strip=True).split()) if price_el else ""
            records.append({
                "nama_akomodasi": name,
                "area": area,
                "rating_bintang_tertera": rating,
                "harga_tertera_idr": price,
                "url_website": website_link or "",
                "url_lokasi": location_link,
                "sumber": page_url,
                "tanggal_akses_utc": datetime.now(timezone.utc).isoformat()
            })

        result["records"] = len(records)
        result["status"] = "SCRAPED" if records else "PAGE_READ_NO_UBUD_PROPERTY_CARDS"
        result["reason"] = (
            "Data diekstrak dari kartu .hotel-item dan difilter area Ubud; "
            "jumlah sesuai halaman yang ditampilkan, bukan total semua hotel di Bali."
        )
        pd.DataFrame(records).to_csv(
            INTERIM / "bali_hotels_association_ubud.csv",
            index=False, encoding="utf-8-sig"
        )
        return result

    except requests.RequestException as exc:
        result["status"] = "REQUEST_FAILED"
        result["reason"] = f"{type(exc).__name__}: {exc}"
        return result


def acquire_overpass() -> dict:
    # Beberapa instance publik digunakan berurutan untuk menghadapi 502/503.
    # Tidak mengirim request paralel; jeda diberikan antar percobaan.
    endpoints = [
        "https://overpass-api.de/api/interpreter",
        "https://overpass.kumi.systems/api/interpreter",
        "https://overpass.private.coffee/api/interpreter",
    ]
    south, west, north, east = -8.57, 115.20, -8.42, 115.34
    q = f"""
[out:json][timeout:60];
(
 node["tourism"~"^(hotel|guest_house|hostel|apartment|chalet|motel|camp_site)$"]({south},{west},{north},{east});
 way["tourism"~"^(hotel|guest_house|hostel|apartment|chalet|motel|camp_site)$"]({south},{west},{north},{east});
 relation["tourism"~"^(hotel|guest_house|hostel|apartment|chalet|motel|camp_site)$"]({south},{west},{north},{east});
);
out center tags;
"""
    errors = []
    payload = None
    selected_endpoint = None
    for attempt, endpoint in enumerate(endpoints, start=1):
        try:
            response = SESSION.post(endpoint, data={"data": q}, timeout=90)
            response.raise_for_status()
            candidate = response.json()
            if "elements" not in candidate:
                raise ValueError("Overpass response has no elements field.")
            payload = candidate
            selected_endpoint = endpoint
            break
        except (requests.RequestException, ValueError) as exc:
            errors.append(f"{endpoint}: {type(exc).__name__}: {exc}")
            if attempt < len(endpoints):
                time.sleep(3 * attempt)

    if payload is None:
        raise RuntimeError("Semua instance Overpass gagal: " + " | ".join(errors))

    save_json(RAW / "openstreetmap_akomodasi_ubud_raw.json", payload)
    rows = []
    for el in payload.get("elements", []):
        tags = el.get("tags", {})
        center = el.get("center", {})
        kind, osm_id = el.get("type", ""), el.get("id")
        rows.append({
            "osm_type": kind,
            "osm_id": osm_id,
            "nama": tags.get("name"),
            "tourism": tags.get("tourism"),
            "alamat": tags.get("addr:street"),
            "desa_atau_suburb": tags.get("addr:suburb") or tags.get("addr:hamlet"),
            "kota": tags.get("addr:city"),
            "latitude": el.get("lat", center.get("lat")),
            "longitude": el.get("lon", center.get("lon")),
            "url_objek": f"https://www.openstreetmap.org/{kind}/{osm_id}"
        })
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["osm_type", "osm_id"])
    df.to_csv(INTERIM / "openstreetmap_akomodasi_ubud.csv", index=False, encoding="utf-8-sig")
    return {
        "status": "SUCCESS",
        "count": len(df),
        "timestamp_osm_base": payload.get("osm3s", {}).get("timestamp_osm_base"),
        "endpoint": selected_endpoint,
        "failed_endpoints": errors
    }

def acquire_weather() -> dict:
    endpoint = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": -8.5069,
        "longitude": 115.2625,
        "start_date": "2025-01-01",
        "end_date": "2025-01-31",
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
        "timezone": "Asia/Makassar"
    }
    response = SESSION.get(endpoint, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    payload = response.json()
    if "daily" not in payload or "time" not in payload["daily"]:
        raise ValueError("Open-Meteo response missing daily/time.")
    save_json(RAW / "open_meteo_ubud_2025-01.json", payload)
    daily = payload["daily"]
    df = pd.DataFrame({
        "tanggal": daily["time"],
        "suhu_rata2_c": daily.get("temperature_2m_mean", []),
        "curah_hujan_mm": daily.get("precipitation_sum", []),
        "kecepatan_angin_maks_kmh": daily.get("wind_speed_10m_max", [])
    })
    df.to_csv(INTERIM / "cuaca_harian_ubud_2025-01.csv", index=False, encoding="utf-8-sig")
    return {"status": "SUCCESS", "count": len(df), "endpoint": endpoint}


def process_base_dataset() -> dict:
    source = INTERIM / "akomodasi_ubud_bps_2015_ekstraksi.csv"
    if not source.exists():
        raise FileNotFoundError(f"Dataset BPS tidak ditemukan: {source}")
    df = pd.read_csv(source)
    required = {"nama_akomodasi", "desa", "kecamatan"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Kolom dataset BPS tidak lengkap: {sorted(missing)}")
    if df.empty:
        raise ValueError("Dataset BPS kosong.")
    if df["nama_akomodasi"].isna().any():
        raise ValueError("Ada nama akomodasi kosong; periksa ekstraksi sumber.")

    by_village = (df.groupby("desa", dropna=False)
                  .agg(jumlah_akomodasi=("nama_akomodasi", "count"))
                  .sort_values("jumlah_akomodasi", ascending=False)
                  .reset_index())
    by_type = (df.groupby("klasifikasi", dropna=False)
               .agg(jumlah_akomodasi=("nama_akomodasi", "count"))
               .sort_values("jumlah_akomodasi", ascending=False)
               .reset_index())
    by_village.to_csv(INTERIM / "analisis_akomodasi_per_desa.csv", index=False, encoding="utf-8-sig")
    by_type.to_csv(INTERIM / "analisis_akomodasi_per_klasifikasi.csv", index=False, encoding="utf-8-sig")

    weather_path = INTERIM / "cuaca_harian_ubud_2025-01.csv"
    if weather_path.exists():
        weather = pd.read_csv(weather_path)
        summary = pd.DataFrame([{
            "kecamatan": "Ubud",
            "periode_cuaca": "2025-01",
            "suhu_rata2_bulanan_c": weather["suhu_rata2_c"].mean(),
            "total_curah_hujan_mm": weather["curah_hujan_mm"].sum(),
            "angin_maks_kmh": weather["kecepatan_angin_maks_kmh"].max()
        }])
        merged = df.merge(summary, on="kecamatan", how="left", validate="many_to_one", indicator=True)
        matched = int((merged["_merge"] == "both").sum())
        unmatched = int((merged["_merge"] != "both").sum())
        merged.drop(columns=["_merge"]).to_csv(
            PROCESSED / "akomodasi_cuaca_ubud.csv", index=False, encoding="utf-8-sig"
        )
    else:
        matched, unmatched = 0, len(df)
    return {
        "bps_rows": len(df),
        "bps_columns": len(df.columns),
        "unique_accommodations": int(df["nama_akomodasi"].nunique()),
        "village_count": int(df["desa"].nunique()),
        "weather_merge_matched": matched,
        "weather_merge_unmatched": unmatched
    }


def write_measurement_and_provenance() -> None:
    # Exclude generated measurement/provenance files to avoid self-referential sizes.
    excluded = {
        "metadata/storage_measurement.csv",
        "metadata/provenance.json",
        "metadata/provenance.csv"
    }
    rows = []
    for path in sorted(BASE_DIR.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(BASE_DIR).as_posix()
        if rel.startswith(".git/") or rel in excluded or "__pycache__" in path.parts:
            continue
        size = path.stat().st_size
        rows.append({
            "path": rel,
            "nama_file": path.name,
            "kategori": rel.split("/")[0] if "/" in rel else "root",
            "ukuran_byte": size,
            "ukuran_kb": round(size / 1024, 3),
            "ukuran_mb": round(size / (1024 ** 2), 6)
        })
    pd.DataFrame(rows).to_csv(META / "storage_measurement.csv", index=False, encoding="utf-8-sig")

    provenance = []
    for row in rows:
        path = BASE_DIR / row["path"]
        digest = hashlib.md5(path.read_bytes()).hexdigest()
        provenance.append({
            **row,
            "md5": digest,
            "waktu_pencatatan_utc": datetime.now(timezone.utc).isoformat()
        })
    (META / "provenance.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    pd.DataFrame(provenance).to_csv(META / "provenance.csv", index=False, encoding="utf-8-sig")


def main() -> None:
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "web_scraping": check_robots_and_scrape_bha()
    }
    try:
        report["openstreetmap"] = acquire_overpass()
    except Exception as exc:
        report["openstreetmap"] = {"status": "FAILED", "error": f"{type(exc).__name__}: {exc}"}

    try:
        report["open_meteo"] = acquire_weather()
    except Exception as exc:
        report["open_meteo"] = {"status": "FAILED", "error": f"{type(exc).__name__}: {exc}"}

    report["dataset_processing"] = process_base_dataset()
    (META / "acquisition_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_measurement_and_provenance()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
