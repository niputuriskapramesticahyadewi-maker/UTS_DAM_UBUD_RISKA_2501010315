# UTS DAM — Akomodasi Ubud

**Mahasiswa:** Ni Putu Riska Pramesti Cahya Dewi  
**NIM:** 2501010315  
**Topik:** Direktori akomodasi Kecamatan Ubud, Kabupaten Gianyar.

## Menjalankan di Google Colab
1. Upload ZIP ini ke Google Colab.
2. Jalankan sel berikut untuk mengekstrak ZIP (ubah nama file jika berbeda):

```python
from zipfile import ZipFile
from pathlib import Path
zip_path = '/content/UTS_DAM_UBUD_RISKA_2501010315_SIAP_COLOAB.zip'
with ZipFile(zip_path) as z: z.extractall('/content')
```

3. Buka notebook di folder `UTS_DAM_UBUD_RISKA_2501010315_FINAL`.
4. Jalankan instalasi dependensi jika diperlukan: `!pip install requests pandas beautifulsoup4 lxml openpyxl`.
5. Jalankan semua sel dari atas. Saat diminta, masukkan **email institusi mahasiswa INSTIKI milikmu**, bukan email humas. Jangan masukkan password.
6. Pastikan file API JSON, robots.txt, HTML (jika diizinkan), hasil merge, dan provenance terbentuk.

## Batasan penting
- Email institusi mahasiswa bersifat individual; tidak dapat ditentukan dari alamat kontak umum kampus. Minta/cek melalui portal mahasiswa atau admin akademik INSTIKI.
- API dan scraping membutuhkan internet saat notebook dijalankan. Notebook tidak menyimpan hasil palsu jika sumber tidak dapat diakses.
- Jika robots.txt melarang URL atau halaman tidak menyediakan tabel HTML statis, scraping tidak dianggap selesai. Pilih sumber statis lain yang diizinkan setelah memeriksa robots.txt, atau konsultasikan ke dosen.
- Data BPS adalah direktori tahun 2015 dalam publikasi 2017; bukan daftar akomodasi saat ini.
- Publikasi BPS menyatakan pembatasan penggandaan/distribusi untuk tujuan komersial tanpa izin tertulis.
- Notebook ini belum memiliki output eksekusi. Simpan ulang setelah menjalankan semua sel tanpa error.
