"""
Modul: main.py
Deskripsi: Titik masuk utama program analisis nilai siswa.
"""
from src.input_data import baca_data_nilai
from src.proses import ringkasan_statistik, status_lulus, BATAS_LULUS
from src.output import simpan_laporan

def main():
    print("=" * 50)
    print("  PROGRAM OTOMATISASI ANALISIS NILAI SISWA")
    print("  Algoritma dan Pemrograman - S1 Pend. Matematika")
    print("=" * 50)

    # 1. Membaca data
    path_data = "data/contoh_data.txt"
    data_siswa = baca_data_nilai(path_data)

    if not data_siswa:
        print("[Info] Data kosong atau gagal dimuat.")
        return

    # 2. Proses statistik
    daftar_angka = [s["nilai"] for s in data_siswa]
    stat = ringkasan_statistik(daftar_angka)

    print(f"\nJumlah Siswa Terdaftar : {stat['jumlah']}")
    print(f"Rata-rata Kelas        : {stat['rata_rata']}")
    print(f"Nilai Tertinggi        : {stat['maksimum']}")
    print(f"Nilai Terendah         : {stat['minimum']}")
    print(f"Siswa Tuntas (KKM {BATAS_LULUS}): {stat['tuntas']} orang")
    print("-" * 50)

    # 3. Evaluasi per siswa & susun teks laporan
    print("\nDaftar Status Ketuntasan Siswa:")
    laporan_teks = "LAPORAN HASIL ANALISIS NILAI KELAS\n" + "="*40 + "\n"
    
    for idx, siswa in enumerate(data_siswa, 1):
        status = status_lulus(siswa["nilai"])
        baris = f"{idx}. {siswa['nama']} - Nilai: {siswa['nilai']} ({status})"
        print(baris)
        laporan_teks += baris + "\n"

    laporan_teks += f"\nRingkasan Statistik:\n" \
                    f"- Rata-rata: {stat['rata_rata']}\n" \
                    f"- Tertinggi: {stat['maksimum']}\n" \
                    f"- Terendah: {stat['minimum']}\n" \
                    f"- Tuntas: {stat['tuntas']} dari {stat['jumlah']} siswa\n"

    # 4. Simpan output laporan
    path_output = "output/laporan_analisis.txt"
    simpan_laporan(path_output, laporan_teks)
    print("\nProgram selesai dieksekusi dengan sukses!")

if __name__ == "__main__":
    main()