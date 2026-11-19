# Panduan finalisasi sebelum pengumpulan

## Status repository
Workflow GitHub Actions terbaru berhasil (**Success**) pada 19 November 2026. Hasil akuisisi sudah disimpan ke repository, jadi tidak perlu menjalankan Google Colab untuk menghasilkan file tambahan ini.

## Hasil yang sudah tersedia
- Dataset BPS: 326 baris, 7 kolom.
- Scraping BHA: 10 kartu hotel Ubud dari halaman pertama (situs menampilkan 1–10 dari 18).
- OpenStreetMap: 849 objek dalam bounding box perkiraan Ubud; JSON mentah dan CSV tersedia.
- Open-Meteo: 31 observasi cuaca Januari 2025; JSON mentah dan CSV tersedia.
- Merge BPS-cuaca: 326 baris cocok, 0 tidak cocok.
- Storage: 14 file data dan metadata diukur, total 4.989.692 byte (sekitar 4,76 MB), tidak termasuk file pengukuran dan provenance.

## Periksa file di GitHub
1. Buka `data/raw/` dan pastikan ada PDF BPS, HTML mentah BHA, JSON mentah OpenStreetMap, dan JSON mentah Open-Meteo.
2. Buka `data/interim/` dan periksa CSV ekstraksi BPS, CSV hasil scraping BHA, CSV OSM, CSV cuaca, serta CSV analisis.
3. Buka `data/processed/akomodasi_cuaca_ubud.csv`.
4. Buka `metadata/acquisition_report.json`, `metadata/storage_measurement.csv`, `metadata/provenance.json`, dan `metadata/provenance.csv`.

## Catatan yang wajib dijelaskan saat presentasi
- Dataset BPS merupakan data historis tahun 2015.
- Scraping BHA mengambil 10 kartu pada halaman pertama dari 18 properti yang ditampilkan situs; jangan menyebutnya seluruh 18.
- Data OSM merupakan sumber API tambahan dalam bounding box perkiraan, bukan direktori resmi dan bukan hasil scraping HTML.
- Data cuaca Januari 2025 berbeda periode dengan dataset BPS tahun 2015.
- BPS tidak di-scrape karena robots.txt menghasilkan HTTP 403; tidak ada upaya melewati pembatasan.
- Atribusi OpenStreetMap: © OpenStreetMap contributors, lisensi ODbL.

## Checklist pengumpulan
- [x] Dataset utama bersumber dari CSV ekstraksi publikasi BPS, bukan data tiruan.
- [x] Scraping HTML BHA dijalankan setelah robots.txt mengizinkan akses.
- [x] HTML mentah scraping disimpan sebelum ekstraksi ke CSV.
- [x] JSON mentah OpenStreetMap disimpan sebelum diolah menjadi CSV.
- [x] JSON mentah Open-Meteo disimpan sebelum diolah menjadi CSV.
- [x] Storage diukur dari ukuran aktual file.
- [x] Provenance mencatat file yang tersedia, ukuran, dan hash MD5.
- [x] Hasil akuisisi dan pengolahan tersimpan di GitHub.
- [ ] Jelaskan keterbatasan cakupan scraping (10 dari 18 properti di halaman).
- [ ] Jelaskan perbedaan periode data BPS dan cuaca.
