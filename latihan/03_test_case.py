# Latihan 3 - Bug Batas Kelulusan
def status_lulus(nilai):
    # Bug awal di modul menggunakan '>'
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    print("Test 59:", status_lulus(59))  # Expected: Tidak lulus
    print("Test 60:", status_lulus(60))  # Expected: Lulus
    print("Test 61:", status_lulus(61))  # Expected: Lulus