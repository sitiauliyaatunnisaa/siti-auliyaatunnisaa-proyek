"""
Modul: output.py
Deskripsi: Menangani pencetakan dan penyimpanan laporan hasil analisis.
"""
import os

def simpan_laporan(filepath, konten_laporan):
    """Menyimpan ringkasan laporan teks ke dalam folder output/file tujuan."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(konten_laporan)
        print(f"[Info] Laporan berhasil disimpan ke: {filepath}")
    except Exception as e:
        print(f"[Error] Gagal menyimpan laporan: {e}")