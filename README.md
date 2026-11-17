# UTS Data Acquisition & Management
## Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud, Gianyar, Bali

### Identitas mahasiswa
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Perguruan Tinggi:** INSTIKI

## Deskripsi proyek
Repository ini berisi pengerjaan UTS mata kuliah **Data Acquisition & Management**. Proyek mengolah direktori akomodasi Kecamatan Ubud dari publikasi BPS, mengambil data cuaca historis Open-Meteo sebagai konteks wilayah, memeriksa akses situs BPS, melakukan penggabungan data, dan menyusun metadata.

Folder utama: `UTS_DAM_UBUD_RISKA_2501010315_FINAL/`.

## Ringkasan data berdasarkan output notebook
- Dataset akomodasi: **104 baris dan 7 kolom**.
- Periode data akomodasi: **2015** (publikasi BPS terbit 2017).
- Data cuaca Open-Meteo: **31 observasi harian**, 1–31 Januari 2025.
- Hasil penggabungan: **104 baris dan 11 kolom**.
- Validasi merge pada output notebook: 104 baris cocok, 0 tidak cocok, dan 0 duplikasi.

Data cuaca Januari 2025 merupakan konteks cuaca wilayah, bukan cuaca pada tahun pendataan akomodasi 2015 dan bukan atribut yang diukur per usaha.

## Struktur repository
- `UTS_DAM_UBUD_RISKA_2501010315_FINAL/UTS_DAM_UBUD_RISKA_2501010315.ipynb` — notebook utama.
- `data/raw/` — PDF sumber BPS dan catatan file mentah.
- `data/interim/` — CSV hasil ekstraksi direktori akomodasi.
- `data/processed/` — CSV hasil penggabungan.
- `metadata/` — checklist etika, provenance, dan metadata.
- `docs/` — dokumentasi dan panduan finalisasi.

## Status akuisisi dan scraping
Output notebook yang tersimpan menunjukkan API Open-Meteo merespons HTTP 200 dan menghasilkan 31 baris data. Namun, file JSON mentah API dan CSV cuaca harian **belum terlihat di repository GitHub saat pemeriksaan**, sehingga keduanya belum dapat dianggap sudah terunggah.

Pemeriksaan `https://bali.bps.go.id/robots.txt` menghasilkan **HTTP 403 Forbidden**. Aturan akses tidak dapat diverifikasi dan scraping tidak dilakukan. HTTP 403 bukan izin untuk melewati pembatasan server. Jangan menyatakan scraping berhasil.

## Cara menjalankan notebook
1. Unduh atau clone repository.
2. Buka notebook utama di Google Colab.
3. Pastikan struktur folder proyek tersedia.
4. Jalankan sel secara berurutan melalui **Runtime → Run all**.
5. Periksa setiap output dan pastikan file keluaran benar-benar terbentuk.
6. Simpan notebook setelah eksekusi agar output terbaru ikut tersimpan.
7. Unggah file keluaran aktual ke folder yang sesuai di repository.

## Pemeriksaan sebelum pengumpulan
- [ ] Pastikan notebook dijalankan ulang dari awal sampai akhir tanpa error.
- [ ] Simpan notebook terbaru beserta output eksekusinya.
- [ ] Unggah JSON mentah Open-Meteo dan CSV cuaca harian jika file tersebut berhasil dibuat.
- [ ] Pastikan provenance mencatat file yang benar-benar ada beserta ukuran dan hash yang sesuai.
- [ ] Pastikan checklist etika CSV dan Excel konsisten.
- [ ] Jelaskan kendala HTTP 403 pada pemeriksaan BPS secara jujur.
- [ ] Pastikan semua tautan dan nama file pada dokumentasi sesuai isi repository.

**Catatan:** angka dan status di README ini mengikuti output notebook yang tersimpan dan pemeriksaan file GitHub. Jika notebook dijalankan ulang dan menghasilkan perubahan, perbarui dokumentasi berdasarkan output terbaru.
