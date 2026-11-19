# Dokumentasi UTS DAM

## Tujuan
Mengakuisisi dan mengelola data direktori akomodasi Ubud dari sumber BPS, melengkapi konteks wilayah dengan data cuaca historis Open-Meteo dan data objek akomodasi OpenStreetMap, serta mendokumentasikan etika dan keterbatasan proses.

## Sumber data
1. BPS Kabupaten Gianyar, *Direktori Hotel Kabupaten Gianyar 2017* (direktori tahun 2015). CSV ekstraksi yang saat ini berada di repository berisi **326 baris data dan 7 kolom**.
2. Open-Meteo Historical Weather API, koordinat Ubud, periode 1–31 Januari 2025.
3. OpenStreetMap melalui Overpass API, objek bertag `tourism` pada bounding box perkiraan sekitar Ubud.
4. Wikipedia bahasa Indonesia melalui MediaWiki API, hanya sebagai data artikel tambahan.

## Proses pengolahan
Dataset BPS divalidasi dan dianalisis langsung dari CSV sumber. Notebook menghitung distribusi akomodasi berdasarkan desa dan klasifikasi tanpa membuat nama hotel/desa tiruan. Data cuaca harian disimpan sebagai JSON mentah dan CSV. Data cuaca diringkas menjadi satu baris konteks wilayah lalu digabungkan ke data akomodasi menggunakan validasi `many_to_one`.

Data OpenStreetMap diambil melalui Overpass API, respons JSON disimpan mentah terlebih dahulu, kemudian elemen `node`, `way`, dan `relation` diekstrak ke CSV. Hasil OSM adalah objek yang tercatat di OpenStreetMap, bukan daftar usaha yang dijamin lengkap atau masih aktif. Bounding box yang digunakan merupakan perkiraan area Ubud, bukan batas administratif resmi Kecamatan Ubud.

## Pemeriksaan scraping BPS
Pemeriksaan `https://bali.bps.go.id/robots.txt` pada eksekusi sebelumnya menghasilkan HTTP 403 Forbidden. Karena aturan akses tidak dapat diverifikasi, scraping halaman BPS tidak dilakukan dan pembatasan server tidak dicoba untuk dilewati. Jika dosen mewajibkan scraping dari situs BPS, mintalah arahan atau persetujuan sumber alternatif yang diperbolehkan.

## Pengukuran storage dan provenance
Notebook mengukur ukuran file yang benar-benar ada menggunakan `stat().st_size`, lalu menyimpan ukuran byte, KB, dan MB dalam `metadata/storage_measurement.csv`. File pengukuran dan provenance dikecualikan dari perhitungan agar tidak terjadi siklus. Provenance mencatat ukuran byte dan hash MD5 file yang tersedia; entri file yang belum terbentuk dilewati.

## Perbedaan periode dan keterbatasan
- Data akomodasi BPS adalah direktori historis tahun 2015, bukan status usaha saat ini.
- Data cuaca berasal dari Januari 2025, sehingga tidak menggambarkan cuaca pada tahun 2015.
- Data OSM bergantung pada kontribusi pemetaan; data dapat tidak lengkap, memiliki atribut kosong, atau berisi objek yang tidak lagi aktif.
- BPS HTTP 403 menyebabkan scraping BPS tidak dilakukan.
- Hasil API dan file provenance hanya dapat dinyatakan tersedia setelah notebook berhasil dijalankan dan keluarannya diunggah ke repository.

## Atribusi
Data OpenStreetMap © OpenStreetMap contributors, tersedia di bawah Open Database License (ODbL). Dokumentasi query: https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide.
