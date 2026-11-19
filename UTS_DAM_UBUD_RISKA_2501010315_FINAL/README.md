# UTS Data Acquisition & Management — Akomodasi Pariwisata Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini mengolah direktori akomodasi Kecamatan Ubud dari publikasi BPS *Direktori Hotel Kabupaten Gianyar 2017* (direktori tahun 2015), melakukan scraping halaman daftar hotel Bali Hotels Association (BHA) yang diizinkan oleh robots.txt, serta mengakuisisi data tambahan dari OpenStreetMap dan Open-Meteo.

## Hasil eksekusi yang tersimpan di GitHub
Eksekusi GitHub Actions berhasil pada 19 November 2026. Ringkasan dari `metadata/acquisition_report.json`:
- Dataset BPS: **326 baris, 7 kolom**, 326 nama akomodasi unik, tersebar pada 8 desa.
- Scraping BHA: **10 kartu hotel Ubud** berhasil diambil dari halaman pertama. Halaman menyatakan 1–10 dari 18, sehingga hasil ini adalah sampel halaman pertama, bukan seluruh 18 properti.
- OpenStreetMap Overpass API: **897 objek** akomodasi pada bounding box perkiraan sekitar Ubud. Respons mentah disimpan sebagai JSON.
- Open-Meteo Historical API: **31 observasi harian** untuk Januari 2025. Respons mentah disimpan sebagai JSON.
- Penggabungan data BPS dengan ringkasan cuaca: **326 baris cocok, 0 tidak cocok**.

## Sumber data
1. **BPS:** PDF publikasi di `data/raw/BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf` dan CSV hasil ekstraksi di `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`.
2. **Bali Hotels Association:** halaman `https://www.balihotelsassociation.com/our-hotel-and-resorts/?location=ubud`. Script memeriksa `robots.txt` terlebih dahulu. Pada eksekusi terakhir robots.txt dan halaman sama-sama merespons HTTP 200, lalu 10 kartu hotel dengan area Ubud diekstrak dari HTML.
3. **OpenStreetMap:** Overpass API mengambil objek bertag akomodasi/pariwisata dalam bounding box perkiraan sekitar Ubud. Data ini merupakan sumber tambahan dan tidak dijamin mencakup semua akomodasi atau batas administratif persis.
4. **Open-Meteo:** Historical Weather API untuk koordinat Ubud (-8.5069, 115.2625), periode 1–31 Januari 2025.

## Empat perbaikan berdasarkan masukan dosen
- Analisis utama memakai dataset BPS hasil ekstraksi sumber publikasi, bukan nama hotel atau desa tiruan.
- Scraping HTML benar-benar dilakukan pada halaman BHA setelah pemeriksaan robots.txt mengizinkan akses. HTML mentah disimpan dan 10 kartu hotel Ubud diekstrak ke CSV. Hasil ini terbatas pada halaman pertama dari 18 properti yang ditampilkan situs.
- Storage diukur dari ukuran aktual file dengan `stat().st_size`, bukan estimasi manual. Pengukuran terakhir mencakup 16 file data dan metadata dengan total **5.051.850 byte (sekitar 4,82 MB)**. File pengukuran, provenance, dan folder `.git` tidak dimasukkan dalam penjumlahan.
- JSON mentah OpenStreetMap dan Open-Meteo disimpan di `data/raw/` sebelum diekstrak menjadi CSV.

## Etika dan batasan
- BPS: pemeriksaan `https://bali.bps.go.id/robots.txt` sebelumnya menghasilkan HTTP 403. Karena aturan akses tidak dapat diverifikasi, scraping BPS tidak dilakukan dan pembatasan tidak dilewati.
- BHA: pada eksekusi terakhir `robots.txt` dan halaman target merespons HTTP 200; script hanya melakukan scraping jika robots.txt dapat dibaca dan mengizinkan halaman.
- OpenStreetMap: cantumkan atribusi **© OpenStreetMap contributors** dan lisensi **ODbL**. Data berasal dari bounding box perkiraan, bukan batas administratif resmi.
- Data BPS merujuk tahun 2015 sedangkan cuaca merujuk Januari 2025. Cuaca hanya menjadi konteks wilayah, bukan cuaca pada saat pendataan BPS.
- Data OSM dan hasil scraping web merupakan data tambahan dan tidak menggantikan dataset historis BPS sebagai dataset utama.

## File keluaran penting
- `data/raw/bali_hotels_association_ubud.html` — HTML mentah halaman BHA.
- `data/raw/openstreetmap_akomodasi_ubud_raw.json` — JSON mentah Overpass.
- `data/raw/open_meteo_ubud_2025-01.json` — JSON mentah Open-Meteo.
- `data/interim/bali_hotels_association_ubud.csv` — hasil scraping 10 kartu hotel Ubud.
- `data/interim/openstreetmap_akomodasi_ubud.csv` — 849 objek OSM.
- `data/interim/cuaca_harian_ubud_2025-01.csv` — 31 observasi cuaca.
- `data/processed/akomodasi_cuaca_ubud.csv` — hasil penggabungan 326 baris.
- `metadata/acquisition_report.json` — status dan jumlah hasil akuisisi.
- `metadata/storage_measurement.csv` — ukuran aktual file.
- `metadata/provenance.json` dan `metadata/provenance.csv` — asal, ukuran, dan hash MD5 file.

## Menjalankan ulang dari GitHub
Buka tab **Actions**, pilih workflow **Akuisisi Data Ubud**, lalu klik **Run workflow**. Workflow akan menginstal dependensi, menjalankan script akuisisi, mengolah dataset, dan menyimpan hasil ke repository. Periksa status akhir workflow dan `metadata/acquisition_report.json`; jangan menganggap akuisisi berhasil jika status API menunjukkan gagal.
