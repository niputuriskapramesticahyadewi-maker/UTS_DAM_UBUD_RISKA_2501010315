# UTS DAM — Akomodasi Pariwisata Kecamatan Ubud

**Mahasiswa:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Struktur folder
- `data/raw/`: PDF BPS asli dan file mentah yang diperoleh saat notebook dijalankan.
- `data/interim/`: CSV ekstraksi direktori dan data perantara.
- `data/processed/`: hasil penggabungan yang dibuat setelah notebook berhasil dijalankan.
- `metadata/`: Data Ethics Checklist, provenance, dan metadata hasil penggabungan.
- `docs/`: dokumentasi serta bukti pemeriksaan scraping.

## Menjalankan notebook di Google Colab
1. Unduh repository sebagai ZIP atau clone repository.
2. Ekstrak folder proyek di Google Colab.
3. Buka `UTS_DAM_UBUD_RISKA_2501010315.ipynb`.
4. Jalankan sel secara berurutan dari awal sampai akhir.
5. Saat diminta, masukkan email institusi mahasiswa INSTIKI yang benar. Email ini dipakai pada User-Agent sesuai instruksi UTS. Jangan masukkan password, API key, atau token.
6. Pastikan request memiliki timeout, User-Agent, jeda antar-request, dan penanganan status/retry.
7. Periksa hasil API Open-Meteo, pemeriksaan `robots.txt`, status scraping, proses merge, provenance, dan metadata.
8. Setelah semua sel selesai, unduh notebook sebagai `.ipynb` dengan output tersimpan, lalu unggah versi yang sudah dijalankan ke GitHub.

## Hal yang perlu diperhatikan
- CSV direktori akomodasi adalah data historis tahun 2015 dari publikasi BPS tahun 2017, bukan daftar usaha yang aktif saat ini.
- Data cuaca Open-Meteo Januari 2025 adalah data kontekstual lokasi, bukan jumlah atau kondisi operasional akomodasi.
- Tabel BPS Provinsi Bali yang dituju merupakan data agregat kabupaten/kota. Jangan menggabungkannya seolah-olah merupakan data tingkat usaha Ubud.
- Scraping hanya dilakukan jika aturan robots.txt dapat diperiksa dan mengizinkan akses. Jika status robots tidak dapat diverifikasi, notebook harus melewati scraping dan mencatat alasannya.
- Hasil API, scraping, dan merge hanya dinyatakan berhasil jika file dan output benar-benar terbentuk saat eksekusi.

## Sebelum dikumpulkan
Periksa bahwa notebook sudah memiliki output, folder `data/raw/` berisi sumber mentah, API menghasilkan minimal 30 baris, bukti robots dan hasil scraping tersedia, file hasil merge tersedia, duplikasi sudah diperiksa, serta provenance memuat URL, tanggal akses, lisensi, dan MD5 untuk setiap file sumber yang benar-benar diperoleh.
