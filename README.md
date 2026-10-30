# Program Otomatisasi Analisis Nilai Ujian Siswa

Proyek akhir ini disusun untuk memenuhi tugas mata kuliah **Algoritma dan Pemrograman** (Program Studi S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa).

## Deskripsi Proyek
Program ini dirancang menggunakan bahasa Python dengan pendekatan **pemrograman modular** (memisahkan fungsi input data, proses logika statistik, dan penyimpanan output)[cite: 3]. Program berfungsi membaca data nilai siswa dari berkas teks eksternal, menghitung statistik kelas (rata-rata, nilai tertinggi, dan terendah), menentukan status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM = 75), serta menyimpan laporan hasil analisis secara otomatis.

## Struktur Direktori Proyek
```text
proyek-akhir-siti-auliyaatunnisaa-2225250085/
│
├── data/
│   └── contoh_data.txt       # Berkas input data mentah siswa
│
├── src/
│   ├── __init__.py           # Penanda modul Python
│   ├── input_data.py         # Modul pembacaan file dengan penanganan error (try-except)
│   ├── proses.py             # Modul logika statistik dan aturan status KKM
│   └── output.py             # Modul penyimpanan laporan hasil analisis
│
├── output/
│   └── laporan_analisis.txt  # Berkas keluaran laporan otomatis
│
├── tests/
│   └── test_case.md          # Dokumen skenario pengujian (test case)
│
├── main.py                   # Titik masuk utama (entry point) program
├── proposal.md               # Dokumen proposal perancangan proyek
├── .gitignore                # Pengaturan berkas yang diabaikan oleh Git
└── README.md                 # Dokumentasi utama proyek
```
# Cara Menjalankan Program
Pastikan Anda sudah menginstal Python di komputer Anda. Buka terminal pada aplikasi VS Code, lalu jalankan perintah berikut di direktori utama proyek:
python main.py

# Anggota Pengembang
Nama: Siti Auliyaatunnisaa
NIM: 2225250085
Program Studi: S1 Pendidikan Matematika