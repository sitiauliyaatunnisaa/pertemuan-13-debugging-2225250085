def hitung_rata_rata(nilai):
    """Menghitung rata-rata dengan aman dan dinamis."""
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    """Menentukan status kelulusan (>= 60)."""
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    """Mencari nilai tertinggi dengan benar."""
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:  # Diperbaiki dari x < tertinggi
            tertinggi = x
    return tertinggi

if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))