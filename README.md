# UTS Data Acquisition & Management

## Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud, Gianyar, Bali

### Identitas
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Perguruan Tinggi:** INSTIKI

### Isi repository
Proyek ini disusun untuk memenuhi UTS mata kuliah Data Acquisition & Management. Folder proyek utama berada di:

`UTS_DAM_UBUD_RISKA_2501010315_FINAL/`

Di dalamnya tersedia:
- Notebook utama untuk mengerjakan soal 1–5.
- PDF publikasi BPS *Direktori Hotel Kabupaten Gianyar 2017* di `data/raw/`.
- CSV ekstraksi direktori akomodasi di `data/interim/`.
- Data Ethics Checklist dalam format CSV dan Excel.
- Dokumentasi proyek dan dependensi Python.

### Catatan penting tentang data utama
CSV ekstraksi berisi **326 baris dan 7 kolom** berdasarkan file yang tersimpan di repository. Data direktori yang dianalisis merujuk pada **tahun 2015**, sedangkan publikasi BPS terbit pada tahun 2017. Karena itu, data ini bersifat historis dan tidak boleh disebut sebagai daftar akomodasi aktif saat ini.

PDF mentah disimpan sebagai sumber asli. CSV merupakan hasil ekstraksi untuk analisis; kolom nomor telepon tidak disertakan dalam CSV turunan. Publikasi BPS memuat pembatasan penggandaan/distribusi untuk tujuan komersial tanpa izin tertulis. Akses unduh publik tidak otomatis berarti lisensi terbuka tanpa batas.

### Cara menjalankan
1. Unduh atau clone repository.
2. Buka notebook `UTS_DAM_UBUD_RISKA_2501010315_FINAL/UTS_DAM_UBUD_RISKA_2501010315.ipynb` di Google Colab.
3. Pastikan folder proyek diekstrak dan file CSV serta PDF berada pada struktur folder aslinya.
4. Jalankan sel dari atas ke bawah.
5. Masukkan email institusi mahasiswa yang benar saat diminta. Jangan memasukkan password atau token.
6. Periksa hasil API, pemeriksaan `robots.txt`, scraping, merge, provenance, dan metadata.
7. Simpan ulang notebook setelah semua sel berhasil dijalankan, sehingga output eksekusi ikut tersimpan.
8. Periksa kembali seluruh file hasil sebelum mengumpulkan URL GitHub melalui ELSA.

### Persyaratan yang harus diverifikasi sebelum pengumpulan
- Dataset utama minimal 100 baris.
- Identifikasi dataset dan estimasi storage sesuai rumus soal.
- Data Ethics Checklist 9 butir dengan bukti.
- Akuisisi API menghasilkan minimal 30 baris.
- Pemeriksaan `robots.txt` dan scraping halaman statis yang diizinkan, dengan bukti nyata.
- Penggabungan minimal dua sumber memakai `merge` dan parameter `validate`.
- Pemeriksaan duplikasi, file hasil penggabungan, metadata hasil, dan provenance (URL, tanggal akses, lisensi, MD5).
- Notebook sudah dijalankan seluruhnya dan output tersimpan.

**Jangan mengarang hasil API, scraping, lisensi, provenance, atau output notebook.** Jika sumber menolak akses atau tidak menyediakan tabel statis, catat keadaan sebenarnya dan selesaikan dengan sumber lain yang diizinkan atau konsultasi kepada dosen.
