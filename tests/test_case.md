```markdown
# Skenario Pengujian (Test Case) - Analisis Nilai Siswa

Dokumen ini mencatat pengujian unit dan integrasi untuk memastikan modul program berjalan dengan benar sesuai standar Pertemuan 15.

| ID | Fitur / Modul | Jenis Uji | Input / Kondisi | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | `proses.py` | Normal | `[70, 80, 90]` pada `hitung_rata_rata()` | Rata-rata = `80.0` | Rata-rata = `80.0` | **PASS** |
| **TC02** | `proses.py` | Boundary | Nilai siswa tepat di angka KKM (`75`) | Status = `Tuntas` | Status = `Tuntas` | **PASS** |
| **TC03** | `proses.py` | Boundary | Nilai siswa di bawah KKM (`74`) | Status = `Remedial` | Status = `Remedial` | **PASS** |
| **TC04** | `input_data.py`| Invalid | Berkas `contoh_data.txt` kosong/tidak ada | Program menangkap error via `try-except` tanpa *crash* | Berhasil ditangani | **PASS** |
| **TC05** | `main.py` | Integrasi | Menjalankan `python3 main.py` | Berkas `output/laporan_analisis.txt` sukses terbentuk | Berkas terbentuk | **PASS** |
3. Tahap Akhir: Uji Coba dan Push ke GitHub