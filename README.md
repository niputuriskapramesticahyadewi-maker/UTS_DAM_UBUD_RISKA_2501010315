# UTS Data Acquisition & Management
## Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud, Gianyar, Bali

### Identitas Mahasiswa
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Perguruan Tinggi:** INSTIKI

---

## 1. Deskripsi Proyek

Proyek ini merupakan pengerjaan Ujian Tengah Semester (UTS) mata kuliah **Data Acquisition & Management**. Fokus proyek adalah mengolah data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali, berdasarkan publikasi Badan Pusat Statistik (BPS).

Proses pengerjaan meliputi pengumpulan dan ekstraksi data, pengambilan data cuaca historis melalui Open-Meteo API, pemeriksaan akses sumber web, pengolahan dan penggabungan data, serta penyusunan metadata dan dokumentasi.

Seluruh file utama proyek disimpan dalam folder:

`UTS_DAM_UBUD_RISKA_2501010315_FINAL/`

## 2. Ringkasan Hasil Pengolahan Data

Berdasarkan hasil yang tercatat pada notebook, diperoleh ringkasan berikut:

| Komponen | Hasil |
|---|---|
| Dataset akomodasi | 104 baris, 7 kolom |
| Tahun data akomodasi | 2015 |
| Tahun publikasi BPS | 2017 |
| Data cuaca Open-Meteo | 31 observasi harian |
| Periode data cuaca | 1–31 Januari 2025 |
| Hasil penggabungan | 104 baris, 11 kolom |
| Data berhasil dicocokkan | 104 baris |
| Data tidak cocok | 0 baris |
| Duplikasi setelah penggabungan | 0 baris |

Penggabungan data dilakukan untuk menghubungkan informasi akomodasi dengan informasi cuaca berdasarkan wilayah Kecamatan Ubud.

**Catatan:** Data akomodasi mengacu pada tahun 2015, sedangkan data cuaca berasal dari Januari 2025. Oleh karena itu, data cuaca hanya digunakan sebagai informasi kontekstual wilayah dan bukan sebagai kondisi cuaca pada tahun pendataan akomodasi.

## 3. Struktur Repository

Struktur folder utama proyek adalah sebagai berikut:

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
    │   ├── interim/
    │   └── processed/
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

Keterangan folder:

- **data/raw/**: menyimpan sumber data mentah, seperti dokumen PDF BPS.
- **data/interim/**: menyimpan data hasil ekstraksi dan data sementara.
- **data/processed/**: menyimpan dataset yang telah melalui proses pengolahan dan penggabungan.
- **metadata/**: menyimpan checklist etika data dan informasi asal-usul data.
- **docs/**: menyimpan dokumentasi dan panduan pengerjaan proyek.

## 4. Sumber Data dan Proses Akuisisi

### A. Data Akomodasi BPS

Sumber data akomodasi berasal dari publikasi BPS berjudul *Direktori Hotel Kabupaten Gianyar 2017*. Data yang digunakan mengacu pada tahun 2015 dan diolah menjadi dataset dengan 104 baris dan 7 kolom.

### B. Data Cuaca Open-Meteo

Data cuaca diperoleh melalui Open-Meteo Historical Weather API untuk wilayah Ubud pada periode 1–31 Januari 2025.

Berdasarkan output notebook, permintaan API berhasil mendapatkan respons HTTP 200 dengan total 31 observasi harian.

### C. Pemeriksaan Akses Website BPS

Pemeriksaan dilakukan terhadap alamat:

`https://bali.bps.go.id/robots.txt`

Hasil pemeriksaan menunjukkan HTTP 403 Forbidden. Karena aturan akses tidak dapat diverifikasi, proses scraping tidak dilanjutkan.

Dengan demikian, proyek ini tidak mengklaim bahwa scraping website BPS berhasil dilakukan.

## 5. Hasil Pengolahan dan Penggabungan

Data akomodasi dan data cuaca diproses menggunakan Python dan Pandas. Setelah proses pengolahan, dilakukan penggabungan data berdasarkan informasi wilayah.

Hasil pemeriksaan pada output notebook menunjukkan:
- Jumlah data sebelum penggabungan: 104 baris.
- Jumlah data setelah penggabungan: 104 baris.
- Data yang berhasil dicocokkan: 104 baris.
- Data yang tidak cocok: 0 baris.
- Duplikasi: 0 baris.

Hasil akhir pengolahan menghasilkan dataset sebanyak **104 baris dan 11 kolom**.

## 6. Cara Menjalankan Notebook

Untuk menjalankan proyek ini melalui Google Colab:

1. Buka repository GitHub dan unduh atau clone repository.
2. Buka folder `UTS_DAM_UBUD_RISKA_2501010315_FINAL/`.
3. Buka file `UTS_DAM_UBUD_RISKA_2501010315.ipynb` menggunakan Google Colab.
4. Pastikan file dan folder data yang dibutuhkan tersedia.
5. Pilih menu **Runtime → Run all** untuk menjalankan seluruh sel notebook.
6. Periksa hasil setiap proses dan pastikan tidak terdapat error.
7. Simpan notebook setelah proses eksekusi selesai.

## 7. Catatan dan Keterbatasan Proyek

Beberapa hal yang perlu diperhatikan dalam proyek ini:

- Data akomodasi merupakan data historis tahun 2015 sehingga belum tentu menggambarkan kondisi usaha akomodasi saat ini.
- Data cuaca berasal dari Januari 2025 sehingga memiliki periode berbeda dengan data akomodasi.
- Pemeriksaan `robots.txt` BPS menghasilkan HTTP 403 Forbidden sehingga scraping tidak dilakukan.
- File JSON mentah Open-Meteo dan CSV cuaca harian belum terlihat di repository saat pemeriksaan. Kedua file tersebut perlu diunggah apabila berhasil dibuat di Google Colab.
- Metadata provenance perlu disesuaikan dengan file yang benar-benar tersedia di repository.

## 8. Checklist Sebelum Pengumpulan

- [ ] Notebook sudah dijalankan dari awal hingga akhir.
- [ ] Tidak terdapat error pada proses utama notebook.
- [ ] Jumlah data sesuai dengan hasil pengolahan terbaru.
- [ ] File sumber PDF dan dataset hasil pengolahan tersedia.
- [ ] File keluaran API diunggah jika berhasil dibuat.
- [ ] Checklist etika data tersedia dalam format CSV dan Excel.
- [ ] Metadata provenance sesuai dengan file yang tersedia.
- [ ] Dokumentasi sesuai dengan hasil aktual proyek.
- [ ] Notebook sudah disimpan dengan output terbaru.

---

**Penutup**

Proyek UTS Data Acquisition & Management ini menerapkan proses akuisisi, pengolahan, penggabungan, dan dokumentasi data menggunakan Python. Hasil pengerjaan diharapkan dapat menunjukkan pemahaman mengenai pengelolaan data, penggunaan API, validasi data, serta penerapan etika dalam proses akuisisi data.
