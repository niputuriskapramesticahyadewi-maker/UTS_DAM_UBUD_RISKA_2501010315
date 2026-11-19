# UTS Data Acquisition & Management — Akomodasi Pariwisata Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini mengolah direktori akomodasi Kecamatan Ubud dari publikasi BPS *Direktori Hotel Kabupaten Gianyar 2017* (direktori tahun 2015), kemudian menambahkan data cuaca historis dan data titik akomodasi dari OpenStreetMap sebagai sumber tambahan.

## Sumber data
1. **BPS:** PDF publikasi di `data/raw/BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf` dan hasil ekstraksi di `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`. Pemeriksaan repository menunjukkan CSV memiliki 326 baris data dan 7 kolom.
2. **Open-Meteo:** Historical Weather API untuk koordinat Ubud (-8.5069, 115.2625), periode 1–31 Januari 2025.
3. **OpenStreetMap:** Overpass API mengambil objek dengan tag pariwisata/akomodasi pada bounding box perkiraan sekitar Ubud. Data ini merupakan sumber tambahan, bukan direktori resmi BPS dan bukan scraping HTML. Kelengkapan bergantung pada data yang dipetakan kontributor.
4. **Wikipedia:** MediaWiki API untuk mencari artikel terkait Ubud. Hasilnya hanya metadata artikel tambahan, bukan daftar akomodasi.

## Perbaikan yang diterapkan pada notebook
- Analisis utama memakai baris aktual CSV BPS, bukan nama hotel atau desa tiruan.
- Ditambahkan akuisisi objek akomodasi dari OpenStreetMap Overpass API. Respons mentah disimpan sebagai JSON sebelum diekstrak menjadi CSV.
- Respons mentah Open-Meteo dan MediaWiki API disimpan sebagai JSON, lalu diturunkan ke CSV.
- Pengukuran storage menghitung ukuran file aktual menggunakan `stat().st_size`, dalam byte, KB, dan MB. File pengukuran dan provenance dikecualikan dari total agar tidak terjadi pengukuran siklik.
- Provenance mencatat file yang benar-benar tersedia, ukuran byte, dan hash MD5.

## Etika dan batasan scraping
Pemeriksaan `https://bali.bps.go.id/robots.txt` sebelumnya menghasilkan HTTP 403. Karena aturan akses tidak dapat diverifikasi, notebook tidak melakukan scraping halaman BPS dan tidak mencoba melewati pembatasan. OpenStreetMap diakses melalui Overpass API sesuai dokumentasi API, bukan dengan mengambil/menyalin halaman HTML. Cantumkan atribusi **© OpenStreetMap contributors** dan lisensi **ODbL**. [Panduan Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide). [Atribusi OpenStreetMap](https://www.openstreetmap.org/copyright).

## Perbedaan periode
Data direktori BPS merujuk tahun 2015, sedangkan cuaca diambil untuk Januari 2025. Karena periodenya berbeda, cuaca hanya menjadi konteks wilayah dan bukan kondisi cuaca saat pendataan akomodasi.

## Keluaran setelah notebook dijalankan
- `data/raw/open_meteo_ubud_2025-01.json`
- `data/raw/wikipedia_ubud_search_raw.json`
- `data/raw/openstreetmap_akomodasi_ubud_raw.json`
- `data/interim/cuaca_harian_ubud_2025-01.csv`
- `data/interim/wikipedia_ubud_articles.csv`
- `data/interim/openstreetmap_akomodasi_ubud.csv`
- `data/interim/analisis_akomodasi_per_desa.csv`
- `data/interim/analisis_akomodasi_per_klasifikasi.csv`
- `data/processed/akomodasi_cuaca_ubud.csv`
- `metadata/storage_measurement.csv`
- `metadata/provenance.json` dan `metadata/provenance.csv`

## Cara menjalankan
1. Buka notebook di Google Colab.
2. Pilih **Runtime → Run all** dan tunggu seluruh sel selesai.
3. Pastikan request API berhasil dan file keluaran benar-benar terbentuk.
4. Periksa jumlah data, hasil validasi merge, ukuran storage, dan provenance.
5. Simpan notebook dengan output terbaru, lalu unggah file keluaran yang dihasilkan ke GitHub.

**Catatan:** Perubahan kode di GitHub belum berarti notebook sudah dieksekusi. File JSON/CSV hasil API baru akan tersedia setelah notebook dijalankan dengan koneksi internet. Jangan membuat file JSON contoh atau menyatakan akuisisi berhasil sebelum respons API benar-benar diterima.
