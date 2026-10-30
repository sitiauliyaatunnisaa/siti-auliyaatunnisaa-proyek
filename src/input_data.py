"""
Modul: input_data.py
Deskripsi: Membaca data mentah dari file eksternal dengan penanganan error.
"""
import os

def baca_data_nilai(filepath):
    """Membaca file teks berisi daftar nilai siswa dengan try-except."""
    data_siswa = []
    
    if not os.path.exists(filepath):
        print(f"[Peringatan] Berkas {filepath} tidak ditemukan.")
        return data_siswa

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split(",")
                    if len(parts) == 2:
                        nama = parts[0].strip()
                        try:
                            nilai = float(parts[1].strip())
                            data_siswa.append({"nama": nama, "nilai": nilai})
                        except ValueError:
                            continue
    except Exception as e:
        print(f"[Error] Terjadi kesalahan saat membaca file: {e}")
        
    return data_siswa