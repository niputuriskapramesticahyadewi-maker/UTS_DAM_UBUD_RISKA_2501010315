# Panduan finalisasi sebelum pengumpulan

Panduan ini mengikuti kondisi file yang terlihat di repository dan output notebook yang tersimpan. Lakukan pemeriksaan ulang setelah menjalankan notebook.

## 1. Jalankan notebook
1. Buka [notebook UTS DAM](../UTS_DAM_UBUD_RISKA_2501010315.ipynb) di GitHub.
2. Pilih **Open in Colab** atau unduh notebook lalu unggah ke Colab.
3. Pastikan folder proyek dan seluruh sumber data tersedia dengan struktur yang benar.
4. Jalankan **Runtime → Run all** dari sel pertama sampai terakhir.
5. Jika muncul error, perbaiki dahulu dan jangan menyatakan tugas selesai sebelum eksekusi berhasil.

## 2. Cocokkan hasil utama
Output notebook yang saat ini tersimpan mencatat:
- Dataset akomodasi: 104 baris dan 7 kolom.
- Data API Open-Meteo: 31 baris harian untuk 1–31 Januari 2025.
- Hasil merge: 104 baris dan 11 kolom.
- Baris cocok: 104; tidak cocok: 0; duplikasi: 0.
- Pemeriksaan robots.txt BPS: HTTP 403; scraping tidak dilakukan.

Angka tersebut harus diperiksa kembali setelah **Run all**. Jangan menggunakan angka 326 baris karena tidak sesuai dengan output notebook yang diperiksa.

## 3. Periksa file keluaran
File berikut belum terlihat di GitHub saat pemeriksaan dan perlu diunggah jika benar-benar terbentuk di Colab:
- `data/raw/open_meteo_ubud_2025-01.json` — respons mentah API.
- `data/interim/cuaca_harian_ubud_2025-01.csv` — data cuaca harian.

File yang sudah terlihat di GitHub:
- `data/raw/BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf`
- `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`
- `data/processed/akomodasi_cuaca_ubud.csv`
- `metadata/data_ethics_checklist.csv`
- `metadata/data_ethics_checklist.xlsx`
- `metadata/provenance.json`

Pastikan provenance mencatat file aktual, ukuran byte, tanggal akses, dan hash yang benar. Jangan menambahkan entri untuk file yang tidak ada.

## 4. Status scraping
Pemeriksaan `https://bali.bps.go.id/robots.txt` menerima HTTP 403 Forbidden. Ini berarti aturan akses tidak dapat diverifikasi. Jangan melakukan scraping atau mencoba melewati pembatasan server dalam kondisi ini. Jika tugas mengharuskan scraping, sampaikan kendala kepada dosen dan minta persetujuan sumber alternatif yang diizinkan.

## 5. Simpan notebook dan unggah
1. Setelah semua sel selesai, pilih **File → Save** atau **File → Download → Download .ipynb**.
2. Pastikan notebook yang diunggah adalah notebook yang baru dijalankan dan outputnya tersimpan.
3. Unggah file JSON dan CSV API jika berhasil dibuat.
4. Periksa kembali struktur folder dan tautan GitHub.

## 6. Checklist akhir
- [ ] Run all selesai tanpa error.
- [ ] Dataset utama 104 baris dan 7 kolom (atau angka terbaru yang benar-benar dihasilkan).
- [ ] Data API minimal 30 baris.
- [ ] File mentah API dan CSV harian diunggah jika tersedia.
- [ ] Merge dan pemeriksaan duplikasi sesuai output aktual.
- [ ] Checklist etika CSV dan Excel konsisten.
- [ ] Provenance sesuai file aktual dan hash terbaru.
- [ ] HTTP 403 dan status scraping dijelaskan dengan jujur.
- [ ] Notebook tersimpan dengan output terbaru.

**Catatan:** memperbaiki README dan dokumentasi tidak otomatis menjalankan notebook. Eksekusi dan pengunggahan keluaran tetap harus dilakukan di Google Colab.
