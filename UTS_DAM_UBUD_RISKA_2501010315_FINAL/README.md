# UTS DAM — Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini disusun untuk memenuhi UTS mata kuliah Data Acquisition & Management. Tahapan meliputi identifikasi dataset, etika data, akuisisi API, pemeriksaan akses web, pengolahan dan penggabungan data, serta dokumentasi metadata dan provenance.

## Ringkasan hasil yang tercatat
- Dataset akomodasi: **104 baris, 7 kolom**; data tahun 2015 dari publikasi BPS tahun 2017.
- API Open-Meteo: **31 observasi harian** untuk 1–31 Januari 2025.
- Hasil merge: **104 baris, 11 kolom**; output notebook menunjukkan 104 cocok, 0 tidak cocok, dan 0 duplikasi.
- Pemeriksaan `robots.txt` BPS: **HTTP 403 Forbidden**; akses tidak dapat diverifikasi dan scraping tidak dilakukan.

Data cuaca 2025 hanya menjadi konteks wilayah dan tidak boleh ditafsirkan sebagai kondisi cuaca pada tahun 2015 atau kondisi spesifik setiap usaha akomodasi.

## Struktur folder
- `data/raw/`: PDF publikasi BPS dan catatan berkas mentah.
- `data/interim/`: CSV ekstraksi direktori akomodasi.
- `data/processed/`: CSV hasil pengolahan/penggabungan.
- `metadata/`: Data Ethics Checklist, provenance, dan metadata hasil.
- `docs/`: dokumentasi dan panduan finalisasi.

## Status file keluaran API
Notebook yang tersimpan menunjukkan respons API berhasil dan 31 baris cuaca terbentuk. Akan tetapi, saat repository diperiksa, file `data/raw/open_meteo_ubud_2025-01.json` dan `data/interim/cuaca_harian_ubud_2025-01.csv` belum ditemukan di GitHub. Unggah kedua file tersebut hanya setelah file aktual berhasil dibuat di Colab.

## Menjalankan notebook di Google Colab
1. Unduh repository sebagai ZIP atau clone repository.
2. Ekstrak folder proyek dengan struktur yang sama.
3. Buka `UTS_DAM_UBUD_RISKA_2501010315.ipynb` di Google Colab.
4. Jalankan **Runtime → Run all** dari awal sampai akhir.
5. Periksa output setiap tahap dan pastikan file keluaran benar-benar terbentuk.
6. Simpan notebook setelah eksekusi agar output ikut tersimpan.
7. Unggah notebook dan file hasil aktual ke GitHub.

## Catatan akses dan scraping BPS
Pemeriksaan `https://bali.bps.go.id/robots.txt` pada output notebook menerima **HTTP 403 Forbidden**. Aturan akses tidak dapat diverifikasi, sehingga scraping tidak dijalankan. Jangan mencoba melewati pembatasan server atau membuat data/tabel scraping pengganti. Jika tugas mewajibkan scraping, konsultasikan kendala ini kepada dosen dan minta persetujuan untuk sumber alternatif.

## Pemeriksaan sebelum dikumpulkan
- [ ] Notebook dijalankan ulang dari awal sampai akhir tanpa error.
- [ ] Dataset utama dan hasil merge sesuai angka aktual.
- [ ] File JSON mentah dan CSV harian API tersedia jika diklaim telah diunggah.
- [ ] Checklist etika diperbarui berdasarkan bukti aktual.
- [ ] Provenance berisi file, ukuran, tanggal, dan hash yang benar.
- [ ] Status robots.txt dan scraping ditulis apa adanya.
- [ ] Semua file yang disebutkan dokumentasi benar-benar tersedia.

**Penting:** perubahan dokumentasi tidak menggantikan eksekusi notebook. Laporkan hanya hasil yang dapat dibuktikan dari output dan file yang tersedia.