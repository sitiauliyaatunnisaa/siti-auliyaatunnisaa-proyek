"""
Modul: proses.py
Deskripsi: Logika perhitungan statistik, rata-rata, dan status kelulusan.
"""

BATAS_LULUS = 75

def hitung_rata_rata(daftar_nilai):
    """Mengembalikan rata-rata list numerik. Mengatasi list kosong."""
    if not daftar_nilai:
        return 0.0
    return sum(daftar_nilai) / len(daftar_nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    """Menentukan status kelulusan siswa berdasarkan KKM."""
    return "Tuntas" if nilai >= batas else "Remedial"

def ringkasan_statistik(daftar_nilai):
    """Menghasilkan dictionary ringkasan statistik kelas."""
    if not daftar_nilai:
        return {
            "jumlah": 0,
            "rata_rata": 0.0,
            "minimum": 0,
            "maksimum": 0,
            "tuntas": 0
        }
    
    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": round(hitung_rata_rata(daftar_nilai), 2),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "tuntas": len([x for x in daftar_nilai if x >= BATAS_LULUS])
    }