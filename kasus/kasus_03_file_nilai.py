# Kasus 3: File I/O Error Handling
try:
    with open("data/nilai.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File tidak ditemukan, periksa kembali path direktori.")