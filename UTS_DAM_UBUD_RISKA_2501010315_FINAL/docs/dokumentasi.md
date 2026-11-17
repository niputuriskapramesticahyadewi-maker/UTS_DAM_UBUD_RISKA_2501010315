# Dokumentasi UTS DAM

## Tujuan
Melakukan akuisisi dan pengelolaan data direktori akomodasi Kecamatan Ubud, melengkapi konteks wilayah dengan data cuaca historis, memeriksa akses sumber web, serta mendokumentasikan proses dan keterbatasannya.

## Sumber data
1. BPS Kabupaten Gianyar, *Direktori Hotel Kabupaten Gianyar 2017*. Dataset yang diekstrak merujuk data tahun 2015.
2. Open-Meteo Historical Weather API, koordinat Ubud, periode 1–31 Januari 2025.
3. BPS Provinsi Bali, halaman tabel statistik akomodasi. Pemeriksaan akses melalui `robots.txt` menerima HTTP 403 sehingga scraping tidak dilakukan.

## Hasil identifikasi dan pengolahan
Berdasarkan output notebook, dataset direktori akomodasi berisi **104 baris dan 7 kolom**: nomor sumber, desa, nama akomodasi, alamat, klasifikasi, kecamatan, dan tahun data. Nomor telepon tidak disertakan pada dataset turunan.

API Open-Meteo menghasilkan **31 observasi harian**. Data cuaca kemudian diringkas menjadi satu baris konteks untuk Kecamatan Ubud dan digabungkan dengan dataset akomodasi menggunakan kolom `kecamatan` serta validasi `many_to_one`.

Output notebook mencatat:
- Baris sebelum merge: 104.
- Baris sesudah merge: 104.
- Baris cocok: 104.
- Baris tidak cocok: 0.
- Duplikasi setelah merge: 0.

Hasil akhir yang dicatat notebook memiliki **104 baris dan 11 kolom**. Data cuaca berasal dari Januari 2025, sedangkan direktori akomodasi merujuk tahun 2015. Karena periodenya berbeda, cuaca hanya merupakan konteks wilayah dan bukan kondisi cuaca saat pendataan akomodasi.

## Pemeriksaan scraping
Permintaan ke `https://bali.bps.go.id/robots.txt` menghasilkan **HTTP 403 Forbidden** pada output notebook. Dengan demikian, aturan akses tidak dapat diverifikasi dan scraping tidak dilakukan. Tidak ada tabel hasil scraping yang dapat dilaporkan. Jangan mencoba melewati pembatasan server atau mengarang hasil scraping.

## Ketersediaan file di GitHub
Pada pemeriksaan repository, PDF BPS, CSV ekstraksi, CSV hasil merge, checklist etika, dan provenance tersedia. File JSON mentah Open-Meteo dan CSV cuaca harian belum terlihat pada folder GitHub yang diperiksa. Karena itu, keduanya belum boleh dinyatakan telah diserahkan melalui repository sampai benar-benar diunggah.

## Keterbatasan
- Dataset akomodasi bersifat historis dan tidak menggambarkan daftar usaha yang pasti masih aktif.
- Data cuaca dan data direktori memiliki periode berbeda.
- HTTP 403 membuat aturan akses BPS tidak dapat diverifikasi; scraping tidak dilakukan.
- Dokumentasi dan provenance harus diperbarui kembali jika notebook dijalankan ulang dan menghasilkan keluaran baru.