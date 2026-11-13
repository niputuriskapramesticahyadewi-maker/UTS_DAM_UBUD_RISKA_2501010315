# UTS Data Acquisition & Management
## Akuisisi Data Akomodasi Pariwisata di Kecamatan Ubud, Gianyar, Bali

### Identitas
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Mata Kuliah:** Data Acquisition & Management
- **Perguruan Tinggi:** INSTIKI

### Tujuan
Proyek ini disusun untuk memenuhi UTS mata kuliah Data Acquisition & Management dengan fokus akuisisi dan pemeriksaan data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali.

### Status pengerjaan
**Repository ini masih berupa kerangka pengerjaan, belum merupakan hasil final UTS.**

Sudah tersedia:
- Notebook Python untuk alur pengerjaan soal 1–5.
- Identitas dan deskripsi topik.
- Referensi awal BPS Kecamatan Ubud.
- Rancangan pemeriksaan kualitas data, provenance, dan etika.
- Rancangan akuisisi data cuaca Open-Meteo sebagai data pendukung.

Masih harus dilengkapi:
1. Dataset resmi direktori usaha akomodasi Kecamatan Ubud minimal 100 baris.
2. Bukti metadata, lisensi, dan ketentuan penggunaan dataset utama.
3. Pemeriksaan PII dan quasi-identifier berdasarkan kolom dataset sebenarnya.
4. URL scraping resmi yang relevan, pemeriksaan robots.txt, dan hasil scraping nyata.
5. Eksekusi notebook dari awal sampai akhir dan penyimpanan seluruh output.

**Jangan mengarang data, lisensi, hasil scraping, atau hasil eksekusi.**

### Sumber awal
1. BPS Kabupaten Gianyar, *Kecamatan Ubud Dalam Angka 2025*:  
   https://gianyarkab.bps.go.id/id/publication/2025/09/26/d7aaf2f580d8d7aa8a34ed93/kecamatan-ubud-dalam-angka-2025.html
2. Open-Meteo Historical Weather API:  
   https://open-meteo.com/en/docs/historical-weather-api

Catatan: tabel BPS agregat jumlah sarana akomodasi per desa bukan direktori daftar usaha 100+ baris. Gunakan hanya sebagai data pendukung, bukan pengganti dataset utama.

### Struktur repository saat ini
```text
UTS_DAM_UBUD_RISKA_2501010315/
├── README.md
└── UTS_DAM_UBUD_RISKA_2501010315/
    ├── README.md
    └── UTS_DAM_UBUD_RISKA_2501010315.ipynb
```

Folder `data/` dan `metadata/` belum ada di repository. Folder tersebut dibuat dan diisi setelah data asli serta hasil proses tersedia.

### Cara menjalankan notebook
1. Buka notebook menggunakan Google Colab.
2. Isi `EMAIL_KAMPUS` dengan email kampus aktif.
3. Siapkan dataset resmi dan simpan sebagai `data/raw/akomodasi_ubud.xlsx`.
4. Periksa dan isi URL scraping yang benar-benar diizinkan.
5. Jalankan semua cell secara berurutan.
6. Simpan data mentah, hasil olahan, provenance, dan checklist etika.

---
**Proyek hanya dapat dinyatakan selesai setelah dataset utama, bukti sumber, hasil proses, dan seluruh persyaratan tugas diverifikasi.**
