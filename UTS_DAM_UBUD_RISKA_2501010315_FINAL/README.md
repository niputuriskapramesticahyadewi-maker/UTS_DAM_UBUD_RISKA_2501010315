# UTS Data Acquisition & Management — Akomodasi Pariwisata Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini mengolah data akomodasi Kecamatan Ubud dari publikasi BPS *Direktori Hotel Kabupaten Gianyar 2017* (data direktori tahun 2015). Data cuaca historis wilayah Ubud diambil melalui Open-Meteo Historical Weather API untuk 1–31 Januari 2025.

## Sumber data
1. **Akomodasi:** `data/interim/akomodasi_ubud_bps_2015_ekstraksi.csv`, hasil ekstraksi publikasi BPS yang disimpan dalam `data/raw/`.
2. **Cuaca:** Open-Meteo Historical Weather API, titik koordinat Ubud (-8.5069, 115.2625), periode 1–31 Januari 2025.
3. **Artikel Wikipedia:** MediaWiki API Wikipedia bahasa Indonesia untuk pencarian artikel terkait Ubud. Sumber ini hanya digunakan sebagai data tambahan informasi wilayah/artikel, bukan direktori resmi akomodasi.

## Perbaikan analisis
- Seluruh statistik akomodasi dihitung dari baris aktual CSV BPS. Tidak ada nama hotel atau desa tiruan yang dibuat untuk analisis.
- Distribusi akomodasi dihitung per desa dan klasifikasi, lalu disimpan sebagai CSV.
- Ukuran penyimpanan dihitung dari ukuran file aktual (`stat().st_size`) dan dilaporkan dalam byte serta KB. Tidak menggunakan estimasi manual.
- Respons mentah Open-Meteo disimpan sebagai JSON sebelum diturunkan menjadi CSV.
- Respons pencarian dan detail artikel Wikipedia disimpan sebagai JSON mentah, sedangkan tabel artikel disimpan sebagai CSV.
- File yang tersedia dicatat dalam provenance dengan ukuran byte dan hash MD5.

## Scraping dan etika
Pemeriksaan `https://bali.bps.go.id/robots.txt` pada eksekusi sebelumnya menghasilkan HTTP 403. Karena aturan akses tidak dapat diverifikasi, notebook tidak melakukan scraping halaman BPS dan tidak mencoba melewati pembatasan. Akuisisi tambahan Wikipedia dilakukan melalui MediaWiki API resmi dengan jeda permintaan. Hasil Wikipedia tidak boleh dianggap sebagai data hotel lengkap.

## Perbedaan periode
Dataset akomodasi BPS berisi data tahun 2015, sedangkan cuaca yang diambil adalah Januari 2025. Karena periodenya berbeda, cuaca hanya digunakan sebagai konteks wilayah dan tidak mewakili kondisi cuaca saat data akomodasi dicatat.

## Struktur keluaran setelah notebook dijalankan
```
data/
├── raw/
│   ├── BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf
│   ├── open_meteo_ubud_2025-01.json
│   ├── wikipedia_ubud_search_raw.json
│   └── robots_bali_bps.txt        (jika berhasil diakses)
├── interim/
│   ├── akomodasi_ubud_bps_2015_ekstraksi.csv
│   ├── cuaca_harian_ubud_2025-01.csv
│   ├── wikipedia_ubud_articles.csv
│   ├── analisis_akomodasi_per_desa.csv
│   └── analisis_akomodasi_per_klasifikasi.csv
└── processed/
    └── akomodasi_cuaca_ubud.csv

metadata/
├── provenance.json
├── provenance.csv
└── storage_measurement.csv
```

## Cara menjalankan
1. Buka notebook `UTS_DAM_UBUD_RISKA_2501010315.ipynb` melalui Google Colab.
2. Jalankan seluruh sel dari awal sampai akhir (**Runtime → Run all**).
3. Pastikan PDF BPS dan CSV ekstraksi tersedia di struktur folder repository.
4. Periksa tabel analisis, ukuran file, status robots.txt, serta jumlah artikel Wikipedia.
5. Pastikan file JSON mentah, CSV turunan, dan provenance benar-benar dihasilkan.
6. Jika ingin menyimpan seluruh hasil ke GitHub, unggah/commit folder keluaran setelah eksekusi berhasil.

**Catatan penting:** menambahkan kode ke repository tidak sama dengan menjalankan notebook. File JSON API dan hasil pengolahan baru menjadi artefak hasil eksekusi setelah notebook dijalankan dengan koneksi internet. Jangan membuat atau mengisi file JSON dengan data contoh.
