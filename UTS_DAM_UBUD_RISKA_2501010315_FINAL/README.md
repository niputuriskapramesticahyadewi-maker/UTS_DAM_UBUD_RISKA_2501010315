# UTS DAM — Akuisisi dan Pengolahan Data Akomodasi Pariwisata Kecamatan Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika  
**Perguruan Tinggi:** INSTIKI

## 1. Deskripsi Proyek

Proyek ini disusun untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah **Data Acquisition & Management (DAM)**.

Tujuan proyek adalah melakukan proses akuisisi dan pengelolaan data akomodasi pariwisata di Kecamatan Ubud. Tahapan pengerjaan meliputi identifikasi sumber data, pemeriksaan etika penggunaan data, ekstraksi data dari dokumen PDF, pengambilan data cuaca melalui API, pemeriksaan akses website, pengolahan dan penggabungan data, serta penyusunan metadata dan provenance.

## 2. Ringkasan Hasil

Berdasarkan hasil yang tercatat pada notebook, diperoleh ringkasan berikut:

| Tahapan | Hasil |
|---|---|
| Dataset akomodasi | 104 baris dan 7 kolom |
| Tahun data akomodasi | 2015 |
| Tahun publikasi BPS | 2017 |
| Akuisisi data cuaca | 31 observasi harian |
| Periode data cuaca | 1–31 Januari 2025 |
| Hasil penggabungan | 104 baris dan 11 kolom |
| Data yang cocok | 104 baris |
| Data yang tidak cocok | 0 baris |
| Duplikasi hasil pemeriksaan | 0 baris |

Data akomodasi bersumber dari publikasi BPS, sedangkan data cuaca diperoleh melalui Open-Meteo Historical Weather API.

**Catatan:** Data cuaca Januari 2025 digunakan sebagai informasi konteks wilayah. Data tersebut tidak menggambarkan kondisi cuaca pada tahun 2015 maupun kondisi cuaca secara khusus di setiap usaha akomodasi.

## 3. Struktur Repository

Struktur folder proyek yang digunakan adalah sebagai berikut:

```text
UTS_DAM_UBUD_RISKA_2501010315/
│
├── README.md
│
└── UTS_DAM_UBUD_RISKA_2501010315_FINAL/
    │
    ├── README.md
    ├── UTS_DAM_UBUD_RISKA_2501010315.ipynb
    ├── requirements.txt
    │
    ├── data/
    │   ├── raw/
    │   │   ├── BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf
    │   │   └── README_raw.txt
    │   │
    │   ├── interim/
    │   │   └── akomodasi_ubud_bps_2015_ekstraksi.csv
    │   │
    │   └── processed/
    │       ├── README.md
    │       └── akomodasi_cuaca_ubud.csv
    │
    ├── metadata/
    │   ├── data_ethics_checklist.csv
    │   ├── data_ethics_checklist.xlsx
    │   └── provenance.json
    │
    └── docs/
        ├── dokumentasi.md
        └── PANDUAN_FINALISASI.md
```

Keterangan:
- `data/raw/` menyimpan dokumen sumber dan catatan data mentah.
- `data/interim/` menyimpan hasil ekstraksi awal dari dokumen sumber.
- `data/processed/` menyimpan dataset yang sudah melalui proses pengolahan dan penggabungan.
- `metadata/` menyimpan checklist etika data dan informasi provenance.
- `docs/` menyimpan dokumentasi serta panduan pengerjaan proyek.

## 4. Sumber Data dan Proses Akuisisi

### A. Data Akomodasi

Data akomodasi diperoleh dari dokumen publikasi BPS berjudul *Direktori Hotel Kabupaten Gianyar 2017*. Data yang digunakan merupakan data tahun 2015 dengan hasil ekstraksi sebanyak 104 baris dan 7 kolom.

### B. Data Cuaca

Data cuaca diperoleh melalui Open-Meteo Historical Weather API untuk periode 1–31 Januari 2025. Hasil akuisisi menghasilkan 31 observasi harian.

### C. Pemeriksaan Akses Website BPS

Pemeriksaan dilakukan terhadap alamat `https://bali.bps.go.id/robots.txt`. Hasil yang tercatat adalah HTTP 403 Forbidden. Karena aturan akses tidak dapat diverifikasi, proses scraping tidak dilanjutkan.

## 5. Hasil Pengolahan dan Penggabungan Data

Data akomodasi dan data cuaca diproses dan digabungkan dalam satu dataset. Berdasarkan output pemeriksaan notebook, hasil penggabungan menghasilkan:
- 104 baris data.
- 11 kolom.
- 104 data cocok.
- 0 data tidak cocok.
- 0 duplikasi berdasarkan pemeriksaan yang dilakukan.

Hasil pengolahan disimpan dengan nama `akomodasi_cuaca_ubud.csv` di dalam folder `data/processed/`.

## 6. Cara Menjalankan Notebook di Google Colab

1. Unduh repository GitHub dalam format ZIP atau lakukan clone repository.
2. Ekstrak repository jika menggunakan file ZIP.
3. Buka file `UTS_DAM_UBUD_RISKA_2501010315.ipynb` melalui Google Colab.
4. Pastikan struktur folder dan lokasi dataset sesuai dengan kode notebook.
5. Pilih menu **Runtime → Run all** untuk menjalankan seluruh tahapan.
6. Periksa hasil setiap proses dan pastikan tidak terdapat error.
7. Simpan notebook setelah seluruh proses selesai agar output terbaru ikut tersimpan.
8. Unggah notebook dan file hasil yang benar-benar terbentuk ke repository GitHub.

## 7. Catatan dan Keterbatasan

1. Data akomodasi menggunakan tahun 2015, sedangkan data cuaca menggunakan Januari 2025. Kedua data memiliki periode berbeda.
2. Pemeriksaan `robots.txt` BPS menghasilkan HTTP 403 Forbidden sehingga aturan akses tidak dapat diverifikasi.
3. Scraping website BPS tidak dilakukan karena akses tidak dapat diverifikasi.
4. File respons mentah API `open_meteo_ubud_2025-01.json` dan file cuaca harian `cuaca_harian_ubud_2025-01.csv` belum ditemukan di repository pada pemeriksaan terakhir.
5. File keluaran API tersebut perlu dibuat dan diunggah terlebih dahulu sebelum dinyatakan tersedia di GitHub.

Apabila tugas mewajibkan scraping, kendala akses BPS perlu dikonsultasikan kepada dosen untuk mendapatkan persetujuan penggunaan sumber alternatif. Pembatasan akses website tidak boleh dilewati.

## 8. Checklist Sebelum Pengumpulan

- [ ] Notebook dijalankan ulang dari awal sampai akhir.
- [ ] Tidak terdapat error pada proses utama notebook.
- [ ] Dataset akomodasi dan hasil penggabungan sesuai dengan output aktual.
- [ ] File keluaran API tersedia jika dinyatakan sudah diunggah.
- [ ] Checklist etika data sesuai dengan kondisi sebenarnya.
- [ ] Provenance mencatat file, ukuran, tanggal, dan hash berdasarkan file aktual.
- [ ] Status pemeriksaan `robots.txt` dan scraping dijelaskan dengan benar.
- [ ] Seluruh file yang disebutkan dalam dokumentasi tersedia di repository.

## 9. Penutup

Proyek ini menunjukkan tahapan akuisisi, pengolahan, penggabungan, dan dokumentasi data menggunakan sumber dokumen PDF serta API. Setiap hasil disajikan berdasarkan output notebook dan file yang tersedia. Keterbatasan akses website dan perbedaan periode data juga dicatat agar proses pengolahan dapat dipahami dan dipertanggungjawabkan.

