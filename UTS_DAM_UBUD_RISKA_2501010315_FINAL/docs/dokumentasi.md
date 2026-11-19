# Dokumentasi UTS DAM — Akomodasi Pariwisata Ubud

## Tujuan
Mengelola data direktori akomodasi Kecamatan Ubud dari publikasi BPS, melakukan scraping halaman daftar hotel BHA sesuai izin robots.txt, mengambil data tambahan melalui API, mengolah hasil, dan mendokumentasikan etika serta provenance.

## Hasil eksekusi terverifikasi
GitHub Actions berhasil dijalankan pada 19 November 2026. Laporan akuisisi terakhir mencatat:
- BPS: 326 baris data, 7 kolom, 326 nama akomodasi unik, 8 desa.
- Scraping BHA: 10 kartu properti Ubud dari halaman pertama. Halaman menampilkan 1–10 dari total 18; karena itu data scraping belum mencakup seluruh halaman.
- OpenStreetMap: 897 objek akomodasi/pariwisata dalam bounding box perkiraan Ubud.
- Open-Meteo: 31 observasi harian untuk Januari 2025.
- Merge dataset BPS dengan ringkasan cuaca: 326 cocok, 0 tidak cocok.

## Sumber dan proses
### 1. Dataset utama BPS
PDF sumber berada di `data/raw/BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf`. CSV hasil ekstraksi berada di `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`. Dataset ini menjadi dasar analisis, bukan data tiruan. Data direktori merujuk tahun 2015.

### 2. Scraping HTML Bali Hotels Association
URL: `https://www.balihotelsassociation.com/our-hotel-and-resorts/?location=ubud`.

Script terlebih dahulu meminta `https://www.balihotelsassociation.com/robots.txt`. Pada eksekusi terakhir, robots.txt merespons HTTP 200 dan halaman target juga HTTP 200. Setelah izin diperiksa, HTML disimpan ke `data/raw/bali_hotels_association_ubud.html`. BeautifulSoup digunakan untuk mengambil kartu properti pada elemen `.hotel-item`, memfilter area Ubud, dan mengekstrak nama akomodasi, rating bintang yang ditampilkan, harga jika tersedia, website, dan tautan lokasi. CSV hasil ekstraksi disimpan di `data/interim/bali_hotels_association_ubud.csv`.

Hasil yang tercatat adalah 10 kartu pada halaman pertama. Situs menunjukkan 1–10 dari 18 properti, jadi hasil belum boleh disebut sebagai seluruh daftar 18 hotel. Data harga/rating adalah informasi yang ditampilkan saat akses dan dapat berubah.

### 3. OpenStreetMap Overpass API
Script mengirim query objek dengan tag `tourism` untuk node, way, dan relation dalam bounding box perkiraan sekitar Ubud. Respons JSON mentah disimpan ke `data/raw/openstreetmap_akomodasi_ubud_raw.json`, lalu diolah menjadi CSV `data/interim/openstreetmap_akomodasi_ubud.csv`. Eksekusi terakhir memperoleh 897 objek. Jumlah ini adalah objek yang dipetakan di OSM dalam area query, bukan jumlah usaha aktif atau daftar resmi. Atribusi: © OpenStreetMap contributors, lisensi ODbL.

### 4. Open-Meteo Historical Weather API
Data cuaca diambil untuk koordinat Ubud, periode 1–31 Januari 2025. JSON mentah disimpan di `data/raw/open_meteo_ubud_2025-01.json` dan CSV turunannya di `data/interim/cuaca_harian_ubud_2025-01.csv`. Terdapat 31 observasi harian.

## Pengolahan dan validasi
CSV BPS diperiksa jumlah baris, kolom, dan keunikan nama akomodasi. Ringkasan akomodasi dibuat per desa dan klasifikasi. Cuaca Januari 2025 diringkas menjadi satu baris konteks wilayah, lalu digabungkan ke data BPS dengan validasi relasi many-to-one. Hasil terakhir menunjukkan 326 baris cocok dan 0 tidak cocok.

**Perbedaan periode:** dataset BPS merujuk tahun 2015, sedangkan cuaca berasal dari Januari 2025. Karena berbeda periode, cuaca tidak boleh ditafsirkan sebagai kondisi cuaca ketika direktori BPS dikumpulkan.

## Pengukuran storage
Pengukuran menggunakan ukuran aktual file dari filesystem (`stat().st_size`). Pengukuran terakhir mencakup 16 file di folder `data/` dan `metadata/` dengan total 5.029.159 byte atau sekitar 4,80 MB. File storage measurement dan file provenance dikecualikan agar tidak terjadi perhitungan siklik. Kode, notebook, dan dokumentasi tidak dicampur ke ukuran dataset.

## Provenance
`metadata/provenance.json` dan `metadata/provenance.csv` mencatat path, sumber, ukuran, waktu pencatatan, dan hash MD5 untuk file yang tersedia. `metadata/acquisition_report.json` mencatat status API/scraping dan jumlah data yang diperoleh.

## Keterbatasan dan etika
- Situs BPS memberikan HTTP 403 pada pemeriksaan robots.txt sebelumnya; scraping BPS tidak dilakukan dan pembatasan tidak dilewati.
- Scraping BHA dilakukan hanya setelah robots.txt dapat dibaca dan mengizinkan akses. Hasil yang diperoleh hanya 10 kartu dari halaman pertama (1–10 dari 18).
- Data OSM bergantung pada kontribusi pemetaan, dapat memiliki atribut kosong, duplikasi nama, atau objek yang tidak lagi aktif.
- Bounding box OSM merupakan perkiraan, bukan batas administratif resmi Kecamatan Ubud.
- Data BPS bersifat historis, tidak menunjukkan status operasional akomodasi saat ini.
- Informasi harga pada halaman BHA dapat berubah dan bukan harga final untuk transaksi.
