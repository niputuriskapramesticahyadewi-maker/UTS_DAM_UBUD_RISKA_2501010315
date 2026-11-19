# UTS DAM — Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika  
**Mata Kuliah:** Data Acquisition & Management  
**Institusi:** INSTIKI

## 1. Deskripsi Proyek

Proyek ini dibuat untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Data Acquisition & Management. Tujuan proyek adalah mengumpulkan, mengolah, dan menganalisis data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali.

Data yang digunakan berasal dari beberapa sumber, yaitu publikasi Badan Pusat Statistik (BPS), Bali Hotels Association (BHA), OpenStreetMap, dan Open-Meteo.

Proyek ini juga menerapkan tahapan pengelolaan data, mulai dari pengumpulan data, penyimpanan data mentah, pembersihan data, pengolahan, hingga analisis.

## 2. Tujuan

1. Mengumpulkan data akomodasi pariwisata di Kecamatan Ubud.
2. Menggunakan sumber data yang dapat ditelusuri.
3. Melakukan proses scraping pada sumber yang memungkinkan.
4. Menggunakan API untuk memperoleh data pendukung.
5. Menyimpan data mentah dalam format JSON.
6. Melakukan pembersihan dan pengolahan data.
7. Menganalisis karakteristik akomodasi berdasarkan data yang tersedia.

## 3. Sumber Data

| Sumber | Data yang Digunakan | Keterangan |
|---|---|---|
| BPS Kabupaten Gianyar | Direktori hotel Kabupaten Gianyar tahun 2017 | Publikasi memuat data akomodasi tahun 2015 |
| Bali Hotels Association | Informasi hotel dan resort di Ubud | Scraping terbatas pada 10 entri yang diperoleh dari halaman pertama |
| OpenStreetMap | Data lokasi akomodasi | Diperoleh melalui Overpass API |
| Open-Meteo | Data cuaca Ubud Januari 2025 | Diperoleh melalui API |

### Dataset BPS

Dataset utama berasal dari publikasi **Direktori Hotel Kabupaten Gianyar 2017**. Data tersebut diekstraksi dan disimpan dalam format CSV.

Berkas hasil ekstraksi:
`data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`

Dataset ini berisi 326 baris data dan 7 kolom. Data tersebut digunakan sebagai dasar analisis akomodasi.

## 4. Metode Akuisisi Data

Proses pengumpulan data dilakukan melalui beberapa metode:

### A. Ekstraksi Data BPS

Data akomodasi diperoleh dari publikasi PDF BPS, kemudian diekstraksi dan disimpan dalam format CSV agar dapat diolah menggunakan Python dan Pandas.

### B. Web Scraping

Scraping dilakukan pada halaman Bali Hotels Association untuk memperoleh informasi hotel dan resort di wilayah Ubud.

Hasil scraping yang tersimpan merupakan 10 entri dari halaman pertama. Data ini tidak diklaim sebagai keseluruhan data pada situs tersebut.

Sebelum pengambilan data, dilakukan pemeriksaan robots.txt dan penerapan jeda permintaan untuk mengurangi beban pada server.

Pengambilan data dari BPS melalui scraping tidak dilakukan karena akses robots.txt menghasilkan respons HTTP 403. Oleh karena itu, data BPS diperoleh melalui ekstraksi publikasi PDF, bukan dengan melewati pembatasan situs.

### C. Akuisisi Data API

Dua API digunakan sebagai data pendukung:

- **OpenStreetMap Overpass API:** untuk memperoleh data lokasi atau objek akomodasi.
- **Open-Meteo API:** untuk memperoleh data cuaca harian di wilayah Ubud pada Januari 2025.

Respons API disimpan dalam format JSON sebagai data mentah sebelum diolah lebih lanjut.

## 5. Struktur Penyimpanan Data

Struktur folder proyek disusun berdasarkan tahapan pengolahan data.

```text
UTS_DAM_UBUD_RISKA_2501010315_FINAL/
│
├── data/
│   ├── raw/
│   │   ├── BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf
│   │   ├── openstreetmap_akomodasi_ubud_raw.json
│   │   ├── open_meteo_ubud_2025-01.json
│   │   └── [berkas mentah hasil scraping BHA]
│   │
│   └── interim/
│       ├── akomodasi_ubud_bps_2015_ekstraksi.csv
│       ├── [berkas hasil pengolahan OpenStreetMap]
│       └── [berkas hasil pengolahan cuaca]
│
├── UTS_DAM_UBUD_RISKA_2501010315.ipynb
├── README.md
└── [berkas pendukung lainnya]
```

**Keterangan:**
- `raw/` digunakan untuk menyimpan data mentah dari sumber asli.
- `interim/` digunakan untuk menyimpan data yang sudah diekstraksi atau diolah sementara.
- Notebook digunakan untuk menjalankan proses akuisisi, validasi, pengolahan, dan analisis data.

## 6. Proses Pengolahan Data

Tahapan pengolahan data meliputi:

1. Mengidentifikasi sumber data.
2. Mengumpulkan data dari sumber yang tersedia.
3. Menyimpan data mentah dalam format aslinya.
4. Mengekstraksi dan mengubah data menjadi format CSV.
5. Memeriksa jumlah baris dan kolom.
6. Memeriksa data kosong dan data duplikat.
7. Memvalidasi nama akomodasi agar tidak menggunakan data placeholder.
8. Melakukan analisis berdasarkan dataset yang telah divalidasi.

Dataset utama yang digunakan dalam analisis adalah:

`data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`

Data tersebut dibaca ke dalam variabel `df_akomodasi` pada notebook.

## 7. Validasi Data

Validasi dilakukan untuk memastikan data yang digunakan sesuai dengan sumbernya.

Pemeriksaan meliputi:

- Jumlah data utama sebanyak 326 baris.
- Jumlah kolom sebanyak 7 kolom.
- Pemeriksaan nilai kosong.
- Pemeriksaan data duplikat.
- Pemeriksaan nama akomodasi.
- Pemeriksaan kesesuaian sumber data.
- Pemeriksaan periode data.

Data placeholder yang mungkin digunakan pada tahap awal pengujian tidak digunakan sebagai dataset utama dalam analisis akhir.

## 8. Analisis Data

Analisis dilakukan menggunakan dataset akomodasi hasil ekstraksi publikasi BPS.

Beberapa aspek yang dapat dianalisis antara lain:

- Jumlah akomodasi berdasarkan wilayah atau desa.
- Karakteristik dan klasifikasi akomodasi.
- Distribusi data akomodasi.
- Data lokasi sebagai informasi pendukung.
- Kondisi cuaca Ubud pada Januari 2025 sebagai konteks tambahan.

**Catatan periode data:** Dataset akomodasi BPS menggunakan data tahun 2015, sedangkan data cuaca Open-Meteo menggunakan periode Januari 2025. Data cuaca tersebut hanya digunakan sebagai informasi pendukung dan bukan sebagai kondisi cuaca pada tahun 2015.

## 9. Estimasi Storage

Ukuran penyimpanan dihitung berdasarkan ukuran berkas aktual menggunakan Python, yaitu melalui fungsi `Path.stat().st_size`.

Perhitungan dilakukan terhadap berkas yang tersedia dalam folder penyimpanan proyek, khususnya data mentah dan data hasil pengolahan.

Rumus perhitungan:

```python
ukuran_kb = ukuran_byte / 1024
ukuran_mb = ukuran_byte / (1024 * 1024)
```

Dengan metode ini, estimasi storage didasarkan pada ukuran berkas sebenarnya, bukan perkiraan jumlah baris atau ukuran rata-rata data.

## 10. Teknologi yang Digunakan

- Python
- Google Colab / Jupyter Notebook
- Pandas
- Requests
- BeautifulSoup
- JSON
- CSV
- OpenStreetMap Overpass API
- Open-Meteo API
- GitHub

## 11. Keterbatasan Proyek

Beberapa keterbatasan dalam proyek ini adalah:

1. Data utama BPS merupakan data tahun 2015 yang berasal dari publikasi tahun 2017.
2. Scraping BHA hanya menghasilkan 10 entri dari halaman pertama, bukan seluruh halaman.
3. Scraping langsung ke sumber BPS tidak dilakukan karena respons akses robots.txt adalah HTTP 403.
4. Data cuaca menggunakan periode Januari 2025 sehingga tidak sama dengan periode dataset utama.
5. Data OpenStreetMap dan BHA digunakan sebagai data pendukung, bukan pengganti dataset utama BPS.

## 12. Kesimpulan

Proyek ini menunjukkan proses akuisisi dan pengelolaan data akomodasi pariwisata di Kecamatan Ubud dengan menggunakan beberapa sumber data.

Dataset utama diperoleh dari publikasi BPS dan diekstraksi menjadi CSV. Data pendukung diperoleh melalui scraping terbatas dan API. Data mentah disimpan dalam format PDF, HTML, dan JSON sesuai sumbernya, sedangkan data hasil pengolahan disimpan dalam format CSV.

Melalui tahapan tersebut, data dapat ditelusuri sumbernya, diperiksa kualitasnya, dan digunakan untuk analisis lebih lanjut.

---

**Repository GitHub:**  
https://github.com/niputuriskapramesticahyadewi-maker/UTS_DAM_UBUD_RISKA_2501010315
