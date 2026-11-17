# UTS Data Acquisition & Management
## Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud, Gianyar, Bali

### Identitas mahasiswa
- **Nama:** Ni Putu Riska Pramesti Cahya Dewi
- **NIM:** 2501010315
- **Program Studi:** Informatika
- **Perguruan Tinggi:** INSTIKI

## Deskripsi proyek
Repository ini berisi pengerjaan Ujian Tengah Semester (UTS) mata kuliah **Data Acquisition & Management** dengan topik data akomodasi pariwisata di Kecamatan Ubud, Kabupaten Gianyar, Bali.

Folder utama proyek: `UTS_DAM_UBUD_RISKA_2501010315_FINAL/`

## Sumber dan gambaran data
Dataset direktori akomodasi yang tersedia di repository memuat **326 baris dan 7 kolom**. Data tersebut merujuk pada tahun **2015**, berdasarkan publikasi BPS yang terbit pada **2017**. Dengan demikian, dataset ini merupakan data historis dan **bukan daftar akomodasi yang dipastikan masih aktif saat ini**.

PDF publikasi disimpan di `data/raw/`, sedangkan CSV hasil ekstraksi tersedia di `data/interim/`. CSV merupakan data turunan untuk analisis. Publikasi sumber mencantumkan ketentuan penggunaan; ketersediaan unduhan publik tidak otomatis berarti seluruh isi bebas digunakan tanpa batas, terutama untuk tujuan komersial.

## Struktur repository
- `UTS_DAM_UBUD_RISKA_2501010315.ipynb` — notebook utama pengerjaan soal.
- `data/raw/` — dokumen sumber dan respons mentah yang benar-benar diperoleh.
- `data/interim/` — dataset ekstraksi dan data perantara.
- `data/processed/` — hasil pengolahan/penggabungan setelah notebook dijalankan.
- `metadata/` — Data Ethics Checklist, provenance, dan metadata hasil.
- `docs/` — dokumentasi, panduan, dan bukti proses scraping.

## Cara menjalankan notebook
1. Clone atau unduh repository sebagai ZIP.
2. Ekstrak folder proyek, lalu buka notebook utama di Google Colab.
3. Pastikan file dan folder proyek berada pada struktur yang sesuai dengan path di notebook.
4. Jalankan sel secara berurutan dari awal sampai akhir (**Runtime → Run all**).
5. Jika notebook meminta email institusi, masukkan alamat email institusi yang benar. Jangan memasukkan password, token, atau informasi rahasia.
6. Periksa output setiap tahap: identifikasi dataset, estimasi storage, checklist etika, API, pemeriksaan akses web, merge, provenance, dan metadata.
7. Simpan notebook setelah dijalankan agar output eksekusinya ikut tersimpan.
8. Unggah kembali notebook beserta file hasil yang benar-benar dihasilkan ke repository.

## Catatan penting: akses robots.txt BPS
Pada pemeriksaan terakhir, permintaan ke `https://bali.bps.go.id/robots.txt` menerima **HTTP 403 Forbidden**. Artinya, aturan akses situs tidak dapat diverifikasi dari respons tersebut. Notebook diarahkan untuk mencatat respons aktual dan **tidak menjalankan scraping BPS ketika robots.txt tidak dapat diperiksa**.

HTTP 403 bukan bukti bahwa scraping diizinkan dan bukan alasan untuk mencoba melewati pembatasan server. Jika akses tetap ditolak, dokumentasikan kendala tersebut dan konsultasikan kepada dosen apakah perlu memakai sumber alternatif yang diizinkan. Jangan menyatakan scraping berhasil jika tabel dan bukti hasilnya tidak benar-benar diperoleh.

## Pemeriksaan sebelum pengumpulan
- [ ] Dataset utama minimal 100 baris dan deskripsi variabel sesuai isi file.
- [ ] Identifikasi dataset dan estimasi kebutuhan penyimpanan dijelaskan dengan asumsi yang transparan.
- [ ] Data Ethics Checklist 9 butir diisi berdasarkan bukti.
- [ ] Akuisisi API menghasilkan minimal 30 baris dan file respons mentah tersimpan.
- [ ] Pemeriksaan `robots.txt` serta status scraping didokumentasikan sesuai respons aktual.
- [ ] Jika scraping tidak dapat dilakukan, kendala dan tindak lanjutnya dijelaskan; jangan membuat data scraping palsu.
- [ ] Penggabungan dua sumber dilakukan hanya jika tingkat detail dan kunci penggabungannya sesuai.
- [ ] Validasi hasil merge, pemeriksaan duplikasi, metadata, dan provenance dilakukan.
- [ ] Notebook dijalankan dari awal sampai akhir dan disimpan dengan output.
- [ ] File hasil yang dirujuk README benar-benar tersedia di repository.

## Status pengerjaan
Kode notebook dan dokumentasi telah mengalami perbaikan. Namun, **perbaikan kode belum sama dengan bukti bahwa seluruh tahapan berhasil dijalankan**. Status akhir API, scraping, merge, provenance, dan metadata harus mengikuti output eksekusi terbaru di Google Colab.

**Prinsip pengerjaan:** hanya laporkan data, hasil, lisensi, dan proses yang benar-benar dapat dibuktikan dari sumber serta file yang tersedia.
