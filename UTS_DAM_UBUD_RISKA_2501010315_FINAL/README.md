# UTS DAM — Akuisisi Data Akomodasi Pariwisata Kecamatan Ubud

**Nama:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Program Studi:** Informatika — INSTIKI

## Tujuan
Proyek ini disusun untuk memenuhi UTS mata kuliah Data Acquisition & Management. Notebook mengerjakan tahapan identifikasi data, estimasi storage, etika data, akuisisi API, pemeriksaan sumber web, pengolahan/penggabungan data, serta dokumentasi metadata dan provenance.

## Struktur folder
- `data/raw/`: PDF publikasi BPS dan respons mentah yang benar-benar diperoleh.
- `data/interim/`: CSV ekstraksi direktori dan data perantara.
- `data/processed/`: hasil pengolahan yang dibuat oleh notebook jika tahap tersebut berhasil.
- `metadata/`: Data Ethics Checklist, provenance, dan metadata hasil.
- `docs/`: dokumentasi dan bukti pemeriksaan akses/scraping.

## Data utama
CSV direktori akomodasi berisi 326 baris dan 7 kolom berdasarkan file yang tersedia di repository. Data direktori merujuk pada tahun 2015 dan diterbitkan dalam publikasi BPS tahun 2017. Data tersebut bersifat historis, bukan daftar usaha yang dipastikan masih aktif saat ini.

Data cuaca Open-Meteo Januari 2025 merupakan data kontekstual cuaca, bukan data jumlah atau status operasional akomodasi. Data agregat tingkat kabupaten/kota tidak boleh diperlakukan sebagai data tingkat usaha di Ubud.

## Menjalankan notebook di Google Colab
1. Unduh repository sebagai ZIP atau clone repository.
2. Ekstrak folder proyek dan pastikan struktur folder tetap sama.
3. Buka `UTS_DAM_UBUD_RISKA_2501010315.ipynb` di Google Colab.
4. Jalankan sel secara berurutan dari awal sampai akhir melalui **Runtime → Run all**.
5. Masukkan email institusi yang benar jika diminta. Jangan masukkan password, token, atau informasi rahasia.
6. Periksa hasil setiap tahap dan pastikan file keluaran benar-benar terbentuk.
7. Simpan atau unduh notebook sebagai `.ipynb` setelah eksekusi agar output ikut tersimpan.
8. Unggah notebook hasil eksekusi dan file keluaran aktual ke GitHub.

## Catatan akses dan scraping BPS
Pada pemeriksaan terakhir, `https://bali.bps.go.id/robots.txt` memberikan respons **HTTP 403 Forbidden**. Respons ini berarti aturan akses tidak dapat diverifikasi. Dalam kondisi tersebut, scraping ke halaman BPS tidak dijalankan. Notebook harus menyimpan catatan status aktual dan melanjutkan tahapan lain yang tidak bergantung pada hasil scraping.

Jangan mencoba melewati pembatasan server dan jangan membuat tabel atau bukti scraping pengganti. Jika tugas mewajibkan scraping, konsultasikan kendala ini kepada dosen dan minta persetujuan untuk memakai sumber alternatif yang aksesnya diizinkan.

## Pemeriksaan sebelum dikumpulkan
- Dataset utama minimal 100 baris.
- Data API minimal 30 baris, dengan file mentah dan hasil olahan.
- Checklist etika diisi berdasarkan bukti.
- Status pemeriksaan robots.txt dan scraping dicatat apa adanya.
- Penggabungan hanya dilakukan pada sumber yang sesuai tingkat detail dan kunci datanya.
- Validasi, pemeriksaan duplikasi, metadata, dan provenance diperiksa.
- Notebook sudah dijalankan dari awal sampai akhir dan output tersimpan.
- Semua file yang disebutkan dalam dokumentasi benar-benar tersedia di repository.

## Status
Notebook dan dokumentasi telah diperbaiki, tetapi keberhasilan seluruh tahapan belum boleh diklaim sebelum output eksekusi terbaru diperiksa. Jika scraping BPS tetap terhalang HTTP 403, catat sebagai kendala akses dan konfirmasikan tindak lanjutnya kepada dosen.

**Catatan:** jangan mengarang hasil API, scraping, merge, lisensi, provenance, atau output. Laporkan hanya hasil yang benar-benar diperoleh.
