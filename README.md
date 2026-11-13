# UTS Data Acquisition & Management
## Akuisisi Data Akomodasi Pariwisata di Kecamatan Ubud, Gianyar, Bali

### Identitas Mahasiswa
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Mata Kuliah:** Data Acquisition & Management
- **Perguruan Tinggi:** INSTIKI

### Deskripsi Proyek
Proyek ini dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Data Acquisition & Management.

Topik yang diangkat adalah akuisisi dan pengolahan data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali.

Proyek ini berfokus pada proses pengumpulan data, pemeriksaan kualitas dan etika data, pengambilan data melalui API, web scraping, serta penggabungan data dari beberapa sumber.

### Tujuan
1. Memahami proses pengumpulan data dari berbagai sumber.
2. Mengidentifikasi struktur dan kualitas dataset.
3. Memahami lisensi serta etika penggunaan data.
4. Mengambil data menggunakan API.
5. Melakukan web scraping sesuai ketentuan situs.
6. Menggabungkan dan memeriksa hasil data.

### Teknologi dan Library
- Python
- Google Colab
- Pandas
- Requests
- BeautifulSoup
- JSON
- GitHub

### Sumber Data
1. **BPS Kabupaten Gianyar**  
   Publikasi Kecamatan Ubud Dalam Angka 2025:  
   https://gianyarkab.bps.go.id/id/publication/2025/09/26/d7aaf2f580d8d7aa8a34ed93/kecamatan-ubud-dalam-angka-2025.html

2. **Open-Meteo Historical Weather API**  
   Digunakan untuk memperoleh data cuaca historis di wilayah Ubud:  
   https://archive-api.open-meteo.com/v1/archive

3. **Sumber web scraping**  
   Halaman statis resmi yang relevan akan dicantumkan setelah pemeriksaan robots.txt dan ketentuan penggunaan situs.

### Struktur Folder
```text
UTS-DAM-Ubud/
│
├── UTS_DAM_UBUD_RISKA_2501010315.ipynb
├── README.md
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
└── metadata/
    ├── provenance.csv
    ├── data_ethics_checklist.xlsx
    └── metadata_hasil_penggabungan.csv
```

### Tahapan Pengerjaan
1. Membaca dan mengidentifikasi dataset akomodasi.
2. Memeriksa lisensi, privasi, dan etika penggunaan data.
3. Mengambil data cuaca menggunakan Open-Meteo API.
4. Memeriksa robots.txt dan melakukan web scraping pada halaman yang diizinkan.
5. Menggabungkan data dan melakukan validasi hasil.

### Cara Menjalankan
1. Buka file notebook menggunakan Google Colab.
2. Isi email kampus pada bagian konfigurasi.
3. Siapkan dataset akomodasi resmi dan simpan pada folder `data/raw/`.
4. Lengkapi URL halaman scraping yang telah diperiksa.
5. Jalankan setiap cell notebook secara berurutan.
6. Periksa hasil pengolahan dan file keluaran.

### Catatan
Notebook ini masih memerlukan pelengkapan dataset utama akomodasi minimal 100 baris, verifikasi lisensi, dan URL scraping yang diizinkan.

Data tidak boleh dibuat-buat atau dimanipulasi untuk memenuhi persyaratan tugas. Seluruh sumber dan proses pengumpulan data harus dicatat dalam metadata provenance.

---
**Dibuat untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Data Acquisition & Management – INSTIKI.**
