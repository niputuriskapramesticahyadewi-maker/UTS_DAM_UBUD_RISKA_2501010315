# Dokumentasi UTS DAM

## Tujuan
Melakukan akuisisi dan pengelolaan data akomodasi Kecamatan Ubud dari publikasi BPS, melengkapi konteks lokasi dengan API cuaca, dan melakukan scraping tabel statistik BPS Provinsi Bali.

## Sumber
1. BPS Kabupaten Gianyar, *Direktori Hotel Kabupaten Gianyar 2017*; tabel yang digunakan merujuk data 2015.
2. Open-Meteo Historical Weather API, koordinat Ubud, 1–31 Januari 2025.
3. BPS Provinsi Bali, tabel statistik akomodasi nonbintang dan akomodasi lainnya menurut kabupaten/kota, 2025.

## Pengolahan
Dataset ekstraksi utama berisi 326 baris dan 7 kolom. Nomor telepon tidak dimasukkan ke dataset turunan. Data API dinormalisasi menjadi observasi harian dan diringkas menjadi satu baris untuk Kecamatan Ubud. Merge menggunakan `kecamatan` dengan `validate='many_to_one'`, kemudian jumlah baris, pasangan, dan duplikasi diperiksa.

## Batasan
Dataset akomodasi bersifat historis (2015). Data cuaca adalah Januari 2025 dan tidak menjelaskan kondisi akomodasi. Tabel scraping BPS merupakan agregat kabupaten/kota sehingga tidak digabung pada tingkat usaha. Scraping hanya boleh dijalankan bila robots.txt mengizinkan.
