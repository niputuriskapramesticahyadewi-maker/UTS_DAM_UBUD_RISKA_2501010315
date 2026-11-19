# Panduan finalisasi sebelum pengumpulan

## 1. Jalankan notebook terbaru
1. Buka notebook UTS DAM dari repository di Google Colab.
2. Pastikan PDF BPS dan CSV ekstraksi tersedia.
3. Pilih **Runtime → Run all**.
4. Pastikan setiap sel selesai tanpa error. Jika Overpass API atau API lain gagal, catat kegagalannya dan jangan mengarang hasil.

## 2. Cocokkan dataset BPS
CSV yang saat ini terlihat di repository berisi **326 baris data dan 7 kolom**. Angka ini berasal dari pemeriksaan file CSV di repository, bukan angka yang diketik manual di notebook. Periksa kembali jumlah baris setelah notebook dijalankan.

## 3. Periksa hasil akuisisi
Jika API berhasil, notebook membuat:
- `data/raw/open_meteo_ubud_2025-01.json`
- `data/raw/wikipedia_ubud_search_raw.json`
- `data/raw/openstreetmap_akomodasi_ubud_raw.json`
- CSV turunan pada folder `data/interim/`

Pastikan JSON mentah benar-benar berisi respons API dan bukan data contoh. Data OSM adalah data objek OpenStreetMap dalam bounding box perkiraan sekitar Ubud, bukan direktori resmi dan bukan scraping HTML.

## 4. Periksa storage dan provenance
Pastikan `metadata/storage_measurement.csv` berisi ukuran aktual byte/KB/MB dari file yang sudah terbentuk. Pastikan `metadata/provenance.json` dan `metadata/provenance.csv` mencatat file yang benar-benar ada, ukuran aktual, dan hash MD5.

## 5. Status scraping BPS
Pemeriksaan `https://bali.bps.go.id/robots.txt` sebelumnya menghasilkan HTTP 403. Scraping BPS tidak dilakukan karena aturan akses tidak dapat diverifikasi. Jangan mencoba melewati pembatasan. Bila dosen mewajibkan scraping, minta persetujuan sumber alternatif.

## 6. Perhatikan perbedaan periode
Direktori BPS merujuk tahun 2015, sedangkan data cuaca diambil untuk Januari 2025. Jelaskan bahwa data cuaca hanya menjadi konteks wilayah, bukan cuaca saat pendataan akomodasi.

## 7. Simpan dan unggah hasil
1. Simpan notebook setelah seluruh sel selesai.
2. Pastikan output eksekusi tersimpan di file `.ipynb`.
3. Unggah JSON mentah, CSV hasil akuisisi, hasil merge, storage measurement, dan provenance yang berhasil dibuat.
4. Buka kembali GitHub dan periksa apakah file benar-benar muncul.

## Checklist
- [ ] Notebook dijalankan dari awal sampai akhir.
- [ ] CSV BPS tervalidasi dan analisis menggunakan data asli.
- [ ] JSON mentah API disimpan sebelum ekstraksi CSV.
- [ ] Data OpenStreetMap diberi atribusi ODbL dan keterbatasan cakupan dijelaskan.
- [ ] Data cuaca dan data akomodasi dijelaskan berbeda periode.
- [ ] Storage diukur dari ukuran file aktual.
- [ ] Provenance berisi file yang tersedia, ukuran byte, dan hash.
- [ ] Notebook terbaru beserta keluaran berhasil diunggah ke GitHub.
