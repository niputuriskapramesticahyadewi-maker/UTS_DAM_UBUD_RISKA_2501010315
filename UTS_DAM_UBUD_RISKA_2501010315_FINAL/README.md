# UTS Data Acquisition & Management — Akomodasi Pariwisata Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini mengolah data akomodasi Kecamatan Ubud dari publikasi BPS *Direktori Hotel Kabupaten Gianyar 2017* (data tahun 2015), serta mengambil data cuaca historis wilayah Ubud melalui Open-Meteo API untuk 1–31 Januari 2025.

## Sumber dan keterbatasan
- Dataset akomodasi: `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`, hasil ekstraksi dari PDF BPS di `data/raw/`.
- Data cuaca: diambil saat notebook dijalankan dari Open-Meteo Historical Weather API. Respons JSON mentah disimpan di `data/raw/open_meteo_ubud_2025-01.json`; CSV harian disimpan di `data/interim/`.
- Pemeriksaan `https://bali.bps.go.id/robots.txt` sebelumnya menghasilkan HTTP 403. Notebook mencatat kendala tersebut dan tidak melanjutkan scraping jika aturan akses tidak dapat diverifikasi.
- Data akomodasi tahun 2015 dan cuaca Januari 2025 berbeda periode. Cuaca hanya konteks wilayah, bukan cuaca historis tahun 2015 atau cuaca tiap hotel.

## Struktur
```
UTS_DAM_UBUD_RISKA_2501010315_FINAL/
├── README.md
├── UTS_DAM_UBUD_RISKA_2501010315.ipynb
├── requirements.txt
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── metadata/
└── docs/
```

## Menjalankan
1. Unduh/clone repository dan pertahankan struktur folder.
2. Buka notebook di Google Colab.
3. Pilih **Runtime → Run all**.
4. Pastikan CSV BPS dan PDF sumber tersedia sebelum menjalankan.
5. Notebook mengambil API secara langsung, membuat file JSON/CSV, menggabungkan data, lalu menghitung MD5 dan provenance.
6. Simpan ulang notebook beserta file output yang benar-benar dihasilkan.

Notebook tidak membuat data hotel tiruan. Jika sumber atau API gagal diakses, proses dihentikan dan kendala dilaporkan. File hasil penggabungan dan provenance akan dibuat ulang ketika notebook berhasil dijalankan; jangan menganggap file keluaran lama sebagai hasil valid.

## Checklist pengumpulan
- [ ] Jalankan ulang notebook dari awal hingga akhir.
- [ ] Periksa hasil validasi dataset dan API.
- [ ] Periksa status robots.txt; jangan melewati pembatasan akses.
- [ ] Pastikan file gabungan, JSON mentah, CSV cuaca, dan provenance dibuat dari eksekusi terbaru.
- [ ] Periksa hash MD5 dan sesuaikan dokumentasi dengan file aktual.
- [ ] Simpan notebook dengan output eksekusi terbaru.
