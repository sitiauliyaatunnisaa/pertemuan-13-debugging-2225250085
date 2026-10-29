# Latihan 4 - Bug Rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)  # Diperbaiki dari hardcode / 5

if __name__ == "__main__":
    print("Rata-rata [80, 90, 70]:", rata_rata([80, 90, 70]))
    print("Rata-rata kosong []:", rata_rata([]))