# UTS Data Acquisition & Management — Akomodasi Pariwisata Kecamatan Ubud

## Identitas Mahasiswa
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Perguruan Tinggi:** INSTIKI
- **Mata Kuliah:** Data Acquisition & Management

## Deskripsi
Repository ini berisi notebook dan struktur kerja UTS mengenai akuisisi data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali. Notebook mencakup pembacaan dataset utama, pemeriksaan etika dan lisensi, akuisisi API Open-Meteo, pemeriksaan `robots.txt` sebelum scraping, serta penggabungan dan validasi data.

## File dan folder
```text
UTS_DAM_UBUD_RISKA_2501010315/
├── README.md
├── UTS_DAM_UBUD_RISKA_2501010315.ipynb
├── data/
│   ├── raw/          # sumber asli, tidak diubah
│   ├── interim/      # hasil normalisasi API/scraping
│   └── processed/    # hasil penggabungan
├── metadata/         # provenance dan checklist etika
└── docs/             # bukti dan catatan pendukung
```

## Sumber yang direncanakan
1. BPS Kabupaten Gianyar, *Kecamatan Ubud Dalam Angka 2025*: https://gianyarkab.bps.go.id/id/publication/2025/09/26/d7aaf2f580d8d7aa8a34ed93/kecamatan-ubud-dalam-angka-2025.html
2. Open-Meteo Historical Weather API: https://archive-api.open-meteo.com/v1/archive
3. Sumber scraping hanya boleh ditambahkan setelah halaman, ketentuan penggunaan, dan `robots.txt` diperiksa. Jangan scraping situs yang dilarang dalam soal UTS.

## Cara menjalankan
1. Buka file `.ipynb` dengan Google Colab.
2. Isi `EMAIL_KAMPUS` dengan email kampus yang benar.
3. Masukkan dataset direktori akomodasi resmi ke `data/raw/akomodasi_ubud.xlsx` (atau sesuaikan path pada notebook). Dataset harus memiliki sekurang-kurangnya 100 baris.
4. Periksa dan isi `URL_TARGET` hanya dengan halaman statis yang relevan dan diizinkan oleh `robots.txt`.
5. Jalankan semua sel secara berurutan dari awal.
6. Periksa output, provenance, checklist, dan file hasil.

## Status kelengkapan — baca sebelum mengumpulkan
**Repository ini adalah paket struktur dan template, bukan bukti bahwa seluruh tugas telah selesai.** Folder `data/raw`, `data/interim`, `data/processed`, dan `docs` disiapkan dengan file penanda. File data asli belum disertakan karena belum diberikan pada saat paket ini dibuat. Jangan menganggap file penanda sebagai dataset.

Sebelum dikumpulkan, lengkapi dan verifikasi:
- [ ] Dataset resmi direktori akomodasi Ubud minimal 100 baris; simpan file asli di `data/raw/`.
- [ ] Lisensi dan ketentuan portal disertai bukti pada `docs/` dan dicatat di `metadata/provenance.csv`.
- [ ] Data API minimal 30 baris tersimpan sebagai respons mentah dan hasil normalisasi.
- [ ] URL scraping, `robots.txt`, izin, dan hasil tabel telah diverifikasi; simpan HTML mentah dan hasilnya.
- [ ] Checklist etika 9 poin diisi dengan status dan bukti nyata, bukan hanya template.
- [ ] Merge minimal dua sumber berhasil, validasi dilakukan, dan tidak ada duplikasi yang tidak dijelaskan.
- [ ] Notebook dijalankan ulang dari awal tanpa error dan disimpan dengan output.
- [ ] Seluruh file hasil dan metadata diunggah ke repository.

## Catatan integritas data
Jangan membuat, menggandakan, atau mengisi data palsu untuk memenuhi jumlah minimum. Tabel ringkasan BPS per desa bukan daftar individual usaha akomodasi 100 baris. Jika data utama belum diperoleh, jelaskan keterbatasan tersebut dan minta data resmi kepada instansi terkait.
