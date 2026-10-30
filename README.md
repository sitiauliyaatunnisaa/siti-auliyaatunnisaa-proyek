# Program Otomatisasi Analisis Nilai Ujian Siswa

Proyek akhir ini disusun untuk memenuhi tugas mata kuliah **Algoritma dan Pemrograman** (Program Studi S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa).

## Deskripsi Proyek
Program ini dirancang menggunakan bahasa Python dengan pendekatan **pemrograman modular** (memisahkan fungsi input data, proses logika statistik, dan penyimpanan output)[cite: 3]. Program berfungsi membaca data nilai siswa dari berkas teks eksternal, menghitung statistik kelas (rata-rata, nilai tertinggi, dan terendah), menentukan status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM = 75), serta menyimpan laporan hasil analisis secara otomatis.

## Tujuan Program
Tujuan pembuatan program ini adalah: Membaca data nilai siswa dari file teks.Memvalidasi data agar hanya nilai yProgram Otomatisasi Analisis Nilai SiswaProyek akhir ini disusun untuk memenuhi tugas mata kuliah Algoritma dan Pemrograman (Program Studi S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa).

## Fitur Program
Fitur yang tersedia meliputi:Membaca data siswa dari file teks.Memeriksa NIM dan nilai siswa.Menolak nilai yang bukan angka atau berada di luar rentang 0–100.Menghindari pemrosesan NIM yang duplikat.Menghitung total dan rata-rata nilai.Menentukan nilai tertinggi dan terendah.Mengelompokkan siswa berdasarkan ketuntasan.Menampilkan hasil analisis di terminal.Menyimpan rekap ke dalam file teks.

## 4. Struktur Folder & Keterangan Modulproyek_nilai/
├── main.py
├── input_data.py
├── data_io.py
├── analisis.py
├── proses.py
├── utilitas.py
├── output.py
├── proposal.md
├── test_case.md
├── README.md
├── .gitignore
├── data/
│   └── contoh_data.txt
└── output/
    └── .gitkeep
Keterangan Fungsi File:main.py: Menjalankan program utama
input_data.py: Menerima input NIM dan nilai siswa
data_io.py: Membaca dan menyimpan data
analisis.py: Menghitung statistik dan ketuntasan
proses.py: Memvalidasi dan memproses data
utilitas.py: Menyediakan fungsi validasi dan format
output.py: Menampilkan dan menyimpan hasil rekap
contoh_data.txt: Menyimpan data contoh siswa
test_case.md: Mendokumentasikan pengujian programp
roposal.md: Menjelaskan rencana dan rancangan program
.gitignore: Mengatur file yang tidak perlu dilacak Git

## 5. Format Data Masukan
Data masukan disimpan di data/contoh_data.txt. Setiap baris menggunakan format:NIM,nilai
Contoh isi file:
A001,85
A002,78
A003,92
A004,abc
A005,60
A006,50
A007,75
A008,88
A009,45
A010,100
(Catatan: Data A004,abc sengaja disertakan untuk menguji validasi nilai yang tidak valid).

## 6. Ketentuan Pengolahan Nilai
Nilai harus berupa angka antara 0 sampai 100.
NIM tidak boleh kosong atau duplikat.
Nilai minimal 60 dinyatakan Tuntas.
Nilai di bawah 60 dinyatakan Belum Tuntas.
Data yang tidak valid tidak dimasukkan dalam perhitungan statistik. 
Jika file tidak ditemukan atau tidak dapat dibaca, program menampilkan pesan kesalahan.

## 7. Cara Menjalankan Program
Pastikan Python telah terpasang di komputer. Buka terminal pada folder utama proyek, kemudian jalankan:
python main.py
Pada beberapa sistem, gunakan:
python3 main.py
Pastikan main.py membaca file yang benar, yaitu data/contoh_data.txt, dan memanggil fungsi pengolahan serta output sesuai nama modul yang digunakan.

## 8. Ringkasan Hasil Pengujian
Berdasarkan data contoh, satu baris tidak valid, yaitu A004,abc. Dengan demikian, terdapat 9 data siswa valid.
KomponenHasilJumlah siswa valid9Total nilai673Rata-rata nilai74,78Nilai tertinggi100Nilai terendah45Siswa tuntas7Siswa belum tuntas2Data tidak valid1Siswa Tuntas: A001, A002, A003, A005, A007, A008, dan A010.Siswa Belum Tuntas: A006 dan A009.

## 9. Skenario Pengujian Program
Pengujian dilakukan untuk memastikan program berjalan sesuai ketentuan.
No.Skenario PengujianHasil yang Diharapkan1Memasukkan nilai 85Data diterima dan berstatus tuntas2Memasukkan nilai 60Data diterima dan berstatus tuntas3Memasukkan nilai 45Data diterima dan berstatus belum tuntas4Memasukkan nilai abcData ditolak5Memasukkan nilai 120Data ditolak6Memasukkan NIM duplikatData duplikat ditolak7Membaca file yang tidak ditemukanPesan kesalahan ditampilkan8Menyimpan hasil rekapFile rekap dibuat jika penyimpanan berhasil

## 10. Analisis Efisiensi
Misalkan $n$ adalah jumlah data siswa yang diproses.
- Proses pembacaan dan pengolahan data dilakukan dengan menelusuri setiap data satu kali.
- Perhitungan total, rata-rata, nilai tertinggi, nilai terendah, dan status ketuntasan memiliki kompleksitas waktu keseluruhan sekitar $\mathcal{O}(n)$, dengan asumsi validasi dan operasi per data berlangsung dalam waktu konstan.
- Penyimpanan data memerlukan ruang tambahan sekitar $\mathcal{O}(n)$ karena data siswa disimpan dalam struktur list untuk diproses.

## 11. Kesimpulan
Program ini membantu proses rekapitulasi dan analisis nilai matematika siswa secara lebih terstruktur. Program menerapkan validasi data, perhitungan statistik, penentuan ketuntasan, serta penyimpanan hasil ke file teks. Melalui proyek ini, konsep dasar pemrograman Python dapat diterapkan dalam penyelesaian masalah pengolahan data nilai siswa.