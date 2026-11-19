# UTS Data Acquisition & Management
## Akuisisi dan Pengelolaan Data Kunjungan Wisatawan Berdasarkan Jenis Wisatawan di Provinsi Nusa Tenggara Barat

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika  
**Perguruan Tinggi:** INSTIKI  
**Mata Kuliah:** Data Acquisition & Management

---

## 1. Deskripsi Proyek

Proyek ini dibuat untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Data Acquisition & Management.

Tujuan proyek adalah melakukan proses akuisisi, pembersihan, pengelolaan, penggabungan, dan dokumentasi data kunjungan wisatawan berdasarkan jenis wisatawan di Provinsi Nusa Tenggara Barat (NTB).

Proyek menggunakan tiga metode akuisisi data:

1. **CSV Dataset:** Mengambil data utama kunjungan wisatawan dari portal Satu Data Provinsi NTB.
2. **API:** Mengambil data cuaca historis menggunakan Open-Meteo Historical Weather API.
3. **Web Scraping:** Mengambil tabel informasi wilayah administratif NTB dari Wikipedia Bahasa Indonesia setelah memeriksa aturan robots.txt.

Data kunjungan wisatawan digabungkan dengan data cuaca berdasarkan tahun dan bulan. Data hasil scraping digunakan sebagai informasi pendukung wilayah dan tidak dipaksakan untuk digabungkan apabila tidak memiliki kunci relasi yang sesuai.

## 2. Sumber Data

### A. Dataset Utama – Satu Data Provinsi NTB

**Nama dataset:** Jumlah Kunjungan Wisatawan berdasarkan Jenis Wisatawan

**Penerbit:** Dinas Pariwisata Provinsi Nusa Tenggara Barat.

**Link sumber dataset:**

https://data.ntbprov.go.id/dataset/9e270f88-a604-4640-a4f0-24c996122b92/show

**Link portal Satu Data NTB:**

https://data.ntbprov.go.id/

Informasi dataset:
- Wilayah: Provinsi Nusa Tenggara Barat.
- Satuan: Orang.
- Penyajian: Bulanan.
- Kategori: Wisatawan Nusantara dan Wisatawan Mancanegara.
- Format sumber: CSV.
- Kolom: Nomor, Kode Provinsi, Nama Provinsi, Kategori Wisatawan, Jumlah (Orang), Tahun, dan Bulan.
- Sumber data: Dinas Pariwisata.

**Catatan:** Halaman portal menampilkan keterangan lisensi `License Not Specified`. Oleh karena itu, izin penggunaan ulang dataset belum dapat dipastikan dan tidak diklaim sebagai data berlisensi terbuka.

### B. Data Cuaca – Open-Meteo Historical Weather API

**Nama layanan:** Open-Meteo Historical Weather API.

**Link dokumentasi API:**

https://open-meteo.com/en/docs/historical-weather-api

**Endpoint API yang digunakan:**

https://archive-api.open-meteo.com/v1/archive

**Link lisensi:**

https://open-meteo.com/en/license

**Link ketentuan layanan:**

https://open-meteo.com/en/terms

Parameter yang digunakan:
- Latitude: `-8.5833`
- Longitude: `116.1167`
- Lokasi: Kota Mataram, Nusa Tenggara Barat.
- `temperature_2m_mean`: Suhu rata-rata harian.
- `precipitation_sum`: Total curah hujan harian.
- `wind_speed_10m_max`: Kecepatan angin maksimum harian.
- Timezone: `Asia/Makassar`.

Data cuaca harian kemudian diolah menjadi data bulanan untuk proses penggabungan dengan dataset kunjungan wisatawan.

**Catatan keterbatasan:** Data cuaca hanya berasal dari satu titik koordinat di Mataram. Data tersebut merupakan data pembanding atau proksi dan tidak mewakili kondisi cuaca seluruh wilayah Provinsi NTB.

Atribusi sumber cuaca: Weather data by Open-Meteo.com.

### C. Data Web Scraping – Wikipedia Bahasa Indonesia

**Sumber halaman scraping utama:**

https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Nusa_Tenggara_Barat

**Sumber halaman alternatif:**

https://id.wikipedia.org/wiki/Nusa_Tenggara_Barat

**Link robots.txt:**

https://id.wikipedia.org/robots.txt

Scraping dilakukan dengan mengambil tabel HTML yang relevan dengan informasi administratif wilayah Nusa Tenggara Barat.

Tahapan scraping:
1. Mengambil file robots.txt.
2. Memeriksa izin akses menggunakan User-Agent.
3. Memeriksa status HTTP halaman.
4. Mengambil tabel HTML menggunakan Pandas.
5. Memilih tabel berdasarkan relevansi informasi.
6. Membersihkan tabel dan menghapus duplikasi.
7. Menyimpan hasil scraping dalam format CSV.

**Catatan:** Pemeriksaan robots.txt merupakan pemeriksaan aturan akses crawler, bukan bukti lisensi konten. Lisensi dan ketentuan atribusi konten Wikipedia harus diperiksa secara terpisah.

## 3. Metode Pengolahan Data

Tahapan pengolahan dalam proyek ini meliputi:

1. **Data Acquisition:** Mengumpulkan dataset utama melalui CSV, data cuaca melalui API, dan tabel wilayah melalui web scraping.
2. **Data Cleaning:** Membersihkan spasi, memperbaiki kesalahan penulisan kategori yang ditemukan, dan mengubah tipe data sesuai kebutuhan.
3. **Data Validation:** Memeriksa jumlah baris, kolom, nilai kosong, kategori, dan konsistensi data.
4. **Data Aggregation:** Mengubah data cuaca harian menjadi data bulanan.
5. **Data Integration:** Menggabungkan dataset kunjungan wisatawan dan data cuaca menggunakan kolom Tahun dan Bulan.
6. **Data Provenance:** Mencatat URL sumber, waktu akses atau unggah, ukuran file, dan MD5.
7. **Final Validation:** Memeriksa hasil pengolahan dan menyiapkan file proyek.

## 4. Struktur Folder Proyek

```text
UTS_DAM_NTB_RISKA_2501010315/
│
├── data/
│   ├── raw/
│   │   ├── dataset_kunjungan_wisatawan.csv
│   │   ├── open_meteo_ntb_historis.json
│   │   ├── wikipedia_robots.txt
│   │   └── wikipedia_ntb.html
│   │
│   ├── interim/
│   │   ├── kunjungan_wisatawan_ntb_bersih.csv
│   │   ├── cuaca_harian_ntb_historis.csv
│   │   └── tabel_wikipedia_ntb_scraping.csv
│   │
│   └── processed/
│       └── kunjungan_wisatawan_ntb_dengan_cuaca.csv
│
├── metadata/
│   ├── identifikasi_dataset.csv
│   ├── klasifikasi_kolom_pii.csv
│   ├── data_ethics_checklist.csv
│   ├── data_ethics_checklist.xlsx
│   ├── provenance.csv
│   ├── metadata_merge.json
│   ├── metadata_scraping.json
│   └── bukti_robots_wikipedia.json
│
├── docs/
│
├── UTS_DAM_NTB_RISKA_2501010315.ipynb
│
└── README.md
```

Nama file CSV di folder `data/raw` mengikuti nama file dataset asli yang diunggah. Struktur di atas merupakan gambaran susunan file yang diharapkan; sesuaikan dengan nama file yang benar-benar dihasilkan notebook.

## 5. Teknologi dan Library

Proyek ini menggunakan:
- Python
- Pandas
- Requests
- BeautifulSoup4
- RobotFileParser
- JSON
- Hashlib
- Jupyter Notebook / Google Colab

Library dapat dipasang menggunakan perintah:

```bash
pip install pandas requests beautifulsoup4 lxml openpyxl
```

Notebook menggunakan fitur unggah dan unduh Google Colab untuk file, sehingga bagian tersebut perlu dijalankan di Google Colab.

## 6. Hasil Pengolahan

Hasil yang diharapkan dari proyek ini meliputi:

| Hasil | Keterangan |
|---|---|
| Dataset mentah | CSV asli dari Satu Data NTB |
| Data bersih | Dataset wisatawan yang telah dibersihkan |
| Data API | Data cuaca harian dari Open-Meteo |
| Hasil scraping | Tabel informasi wilayah NTB |
| Hasil merge | Dataset wisatawan yang dilengkapi variabel cuaca bulanan |
| Metadata | Identifikasi dataset dan informasi pengolahan |
| Provenance | Catatan asal-usul dan integritas file |
| Data ethics | Checklist etika penggunaan data |

Hasil angka, jumlah baris, rentang waktu, dan ukuran file mengikuti data aktual yang berhasil diperoleh ketika notebook dijalankan. Nilai tersebut tidak ditetapkan secara manual dalam README ini.

## 7. Cara Menjalankan Notebook

1. Buka Google Colab: https://colab.research.google.com/
2. Unggah file notebook `.ipynb`.
3. Siapkan dan unggah file CSV dataset utama dari Satu Data NTB ketika diminta.
4. Jalankan setiap sel secara berurutan dari Sel 1 sampai Sel 9.
5. Periksa hasil akuisisi CSV, API, dan scraping.
6. Periksa hasil pembersihan dan penggabungan data.
7. Pastikan file metadata dan provenance berhasil dibuat.
8. Unduh file ZIP hasil proyek setelah proses validasi selesai.

## 8. Etika dan Keterbatasan Data

Beberapa hal yang diperhatikan dalam proyek ini:

- Dataset utama merupakan data agregat kunjungan wisatawan, bukan data identitas individu.
- Lisensi dataset utama masih berstatus `License Not Specified`.
- Ketentuan penggunaan portal perlu diperiksa secara terpisah.
- Data cuaca hanya menggunakan satu titik koordinat di Mataram.
- Hasil scraping dilakukan setelah pemeriksaan robots.txt.
- Robots.txt tidak dapat dijadikan pengganti pemeriksaan lisensi konten.
- Data mentah disimpan terpisah dari data hasil pembersihan.
- Data yang tidak tersedia atau belum terverifikasi tidak dibuat-buat.

## 9. Referensi Sumber

1. Satu Data Provinsi Nusa Tenggara Barat. *Jumlah Kunjungan Wisatawan berdasarkan Jenis Wisatawan*.  
   https://data.ntbprov.go.id/dataset/9e270f88-a604-4640-a4f0-24c996122b92/show

2. Open-Meteo. *Historical Weather API Documentation*.  
   https://open-meteo.com/en/docs/historical-weather-api

3. Open-Meteo. *API License*.  
   https://open-meteo.com/en/license

4. Open-Meteo. *Terms and Conditions*.  
   https://open-meteo.com/en/terms

5. Wikipedia Bahasa Indonesia. *Daftar Kabupaten dan Kota di Nusa Tenggara Barat*.  
   https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Nusa_Tenggara_Barat

6. Wikipedia Bahasa Indonesia. *Nusa Tenggara Barat*.  
   https://id.wikipedia.org/wiki/Nusa_Tenggara_Barat

7. Wikipedia. *Robots.txt*.  
   https://id.wikipedia.org/robots.txt

---

## 10. Penutup

Proyek ini menerapkan tahapan dasar Data Acquisition & Management mulai dari pengumpulan data, pemeriksaan sumber, pembersihan, penggabungan, hingga dokumentasi provenance.

Melalui proyek ini, diharapkan proses pengelolaan data dapat dilakukan secara terstruktur, dapat ditelusuri sumbernya, dan memperhatikan etika serta keterbatasan data yang digunakan.

**Disusun untuk memenuhi UTS Data Acquisition & Management — INSTIKI.**
