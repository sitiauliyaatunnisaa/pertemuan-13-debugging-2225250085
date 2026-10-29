# Latihan 2 - Menelusuri Fungsi
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

if __name__ == "__main__":
    hasil = hitung_diskon(200000, 10)
    print("Hasil diskon:", hasil)