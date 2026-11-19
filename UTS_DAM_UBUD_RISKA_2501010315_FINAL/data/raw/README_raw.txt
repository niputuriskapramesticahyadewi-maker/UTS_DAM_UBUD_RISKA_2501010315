Folder ini menyimpan file sumber mentah yang benar-benar dihasilkan atau digunakan oleh proyek.

File yang tersedia setelah workflow GitHub Actions berhasil:
- BPS5104-direktori_hotel_kabupaten_gianyar_2017.pdf — publikasi sumber BPS.
- bali_hotels_association_ubud.html — HTML mentah halaman daftar hotel BHA; robots.txt dan halaman target merespons HTTP 200 saat pengambilan.
- openstreetmap_akomodasi_ubud_raw.json — respons mentah Overpass API, 897 objek pada eksekusi terakhir.
- open_meteo_ubud_2025-01.json — respons mentah Open-Meteo, 31 observasi harian.

Scraping BHA menghasilkan 10 kartu hotel area Ubud dari halaman pertama (1–10 dari 18 properti yang ditampilkan). Scraping BPS tidak dilakukan karena pemeriksaan robots.txt BPS menghasilkan HTTP 403 dan aturan akses tidak dapat diverifikasi.

Lihat metadata/acquisition_report.json untuk status serta jumlah hasil terbaru. Jangan menganggap jumlah data selalu sama pada setiap eksekusi karena data API dapat berubah.
