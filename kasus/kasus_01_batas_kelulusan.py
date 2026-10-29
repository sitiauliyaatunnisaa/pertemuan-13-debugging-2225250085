# Kasus 1: Batas Kelulusan (Logical Error pada operator)
nilai = 60
# Bug awal: menggunakan > 60 sehingga nilai tepat 60 dianggap tidak lulus
if nilai >= 60:
    print("Status: Lulus")
else:
    print("Status: Tidak Lulus")