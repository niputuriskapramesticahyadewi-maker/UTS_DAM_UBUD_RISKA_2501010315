"""
Scraping metadata dan ringkasan artikel Wikipedia terkait Ubud dan akomodasi.
Sumber: MediaWiki Action API Wikipedia bahasa Indonesia.
Catatan: hasilnya adalah artikel Wikipedia, BUKAN direktori lengkap hotel.
"""

from pathlib import Path
from datetime import datetime, timezone
import json
import time
import requests
import pandas as pd

API_URL = "https://id.wikipedia.org/w/api.php"
OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

KEYWORDS = [
    "Ubud",
    "hotel di Ubud",
    "penginapan Ubud",
    "akomodasi Ubud",
    "resor Ubud",
    "villa Ubud",
]

HEADERS = {
    "User-Agent": "UTS-DAM-Ubud-Student-Research/1.0 (Wikipedia data collection)"
}

session = requests.Session()
session.headers.update(HEADERS)


def search_articles(keyword: str) -> list[dict]:
    """Mencari artikel Wikipedia berdasarkan kata kunci."""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "srlimit": 20,
        "format": "json",
    }
    response = session.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json().get("query", {}).get("search", [])


def get_article(page_id: int) -> dict:
    """Mengambil judul, isi teks, dan URL artikel berdasarkan page ID."""
    params = {
        "action": "query",
        "pageids": page_id,
        "prop": "extracts|info",
        "explaintext": 1,
        "inprop": "url",
        "format": "json",
    }
    response = session.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    pages = response.json().get("query", {}).get("pages", {})
    return pages.get(str(page_id), {})


def main() -> None:
    records = []
    seen_page_ids = set()

    for keyword in KEYWORDS:
        print(f"Mencari artikel: {keyword}")
        try:
            search_results = search_articles(keyword)
        except requests.RequestException as exc:
            print(f"Pencarian gagal untuk '{keyword}': {exc}")
            continue

        for item in search_results:
            page_id = item.get("pageid")
            if page_id is None or page_id in seen_page_ids:
                continue

            seen_page_ids.add(page_id)

            try:
                article = get_article(page_id)
                if not article:
                    continue

                records.append({
                    "keyword_pencarian": keyword,
                    "judul": article.get("title", ""),
                    "page_id": page_id,
                    "ringkasan": article.get("extract", ""),
                    "url_sumber": article.get("fullurl", ""),
                    "tanggal_akuisisi_utc": datetime.now(
                        timezone.utc
                    ).isoformat(),
                })
                time.sleep(1)  # jeda wajar antarpermintaan

            except requests.RequestException as exc:
                print(f"Gagal mengambil page_id {page_id}: {exc}")

    columns = [
        "keyword_pencarian",
        "judul",
        "page_id",
        "ringkasan",
        "url_sumber",
        "tanggal_akuisisi_utc",
    ]
    df = pd.DataFrame(records, columns=columns)

    csv_path = OUTPUT_DIR / "wikipedia_akomodasi_ubud.csv"
    json_path = OUTPUT_DIR / "wikipedia_akomodasi_ubud.json"

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    df.to_json(json_path, orient="records", force_ascii=False, indent=2)

    print("\n=== RINGKASAN AKUISISI ===")
    print(f"Jumlah artikel unik: {len(df)}")
    print(f"CSV tersimpan: {csv_path}")
    print(f"JSON tersimpan: {json_path}")
    if not df.empty:
        print(df[["judul", "url_sumber"]].to_string(index=False))
    else:
        print("Tidak ada artikel yang berhasil diperoleh. Periksa koneksi/API.")


if __name__ == "__main__":
    main()
