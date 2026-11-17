# Panduan finalisasi sebelum pengumpulan

Ikuti langkah ini setelah perubahan notebook terbaru tersedia di GitHub.

## 1. Jalankan notebook
1. Buka [notebook UTS DAM](../UTS_DAM_UBUD_RISKA_2501010315.ipynb) di GitHub.
2. Pilih **Open in Colab**.
3. Pastikan folder proyek tersedia di sesi Colab. Jika menggunakan ZIP, unggah dan ekstrak ZIP terlebih dahulu.
4. Jalankan **Runtime → Run all** dari sel pertama sampai terakhir.
5. Jika muncul error, jangan lanjut menyatakan tugas selesai. Catat pesan error dan perbaiki penyebabnya.

## 2. Periksa hasil yang wajib terbentuk
- `data/interim/cuaca_harian_ubud_2025-01.csv`: minimal 30 baris.
- `data/raw/open_meteo_ubud_2025-01.json`: respons JSON mentah API.
- `data/raw/robots_bali_bps.txt`: respons robots.txt yang benar-benar diterima.
- `docs/bukti_scraping.txt`: status pemeriksaan dan scraping aktual.
- `data/processed/akomodasi_cuaca_ubud.csv`: hasil merge.
- `metadata/provenance.csv`: sumber, URL, tanggal akses, lisensi/pembatasan, ukuran, dan MD5.
- `metadata/metadata_hasil_penggabungan.csv`: metadata hasil merge.

Jika robots.txt melarang akses atau halaman tidak menyediakan tabel statis, simpan status tersebut sebagai hasil sebenarnya. Jangan membuat file HTML/tabel tiruan.

## 3. Simpan notebook dengan output
Di Colab pilih **File → Save** atau **File → Download → Download .ipynb**. Pastikan notebook yang diunggah ke GitHub adalah versi yang sudah memiliki output eksekusi, bukan notebook kosong tanpa output.

## 4. Unggah hasil ke GitHub
Unggah notebook yang sudah dijalankan beserta file keluaran yang benar-benar terbentuk ke folder proyek dengan struktur yang sama. Jangan unggah file kosong atau hasil contoh.

## 5. Pemeriksaan terakhir
- Dataset utama tetap 326 baris dan 7 kolom.
- API menghasilkan minimal 30 baris.
- Merge memakai `validate='many_to_one'` dan tidak menambah/menghilangkan baris secara tidak terduga.
- Duplikasi diperiksa.
- Metadata dan provenance dibuat dari file yang benar-benar ada.
- Status scraping ditulis sesuai bukti.
- Notebook tersimpan dengan output.

**Catatan:** perubahan kode di GitHub tidak sama dengan bukti notebook sudah dijalankan. Eksekusi di Colab dan penyimpanan output tetap harus dilakukan pada sesi Colab.
