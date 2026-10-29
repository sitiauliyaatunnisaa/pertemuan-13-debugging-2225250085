# Kasus 2: Perhitungan Rata-rata (Hardcode pembagi)
nilai_list = [80, 75, 90]
# Bug awal: membagi dengan angka tetap (misal / 5), padahal jumlah data dinamis
if len(nilai_list) > 0:
    rata_rata = sum(nilai_list) / len(nilai_list)
    print(f"Rata-rata: {rata_rata}")
else:
    print("List kosong")