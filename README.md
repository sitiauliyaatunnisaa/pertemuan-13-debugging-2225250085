# Pertemuan 13 - Debugging dan Testing
* **Nama:** Aurda
* **NIM:** 2225250085
* **Kelas:** S1 Pendidikan Matematika

## Kasus
Program yang diuji adalah skrip pemrosesan data nilai mahasiswa yang sengaja dirancang memiliki beberapa bug (kesalahan logika). Program ini terdiri dari tiga fungsi utama, yaitu fungsi untuk menghitung rata-rata nilai, menentukan status kelulusan berdasarkan batas angka, dan mencari nilai tertinggi dari sekumpulan data list.

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | rata-rata | `[80, 60, 90, 70]` | `75.0` | `60.0` | **FAIL** |
| **T2** | rata-rata | `[100, 80]` | `90.0` | `36.0` | **FAIL** |
| **T3** | status | `60` | `Lulus` | `Tidak lulus` | **FAIL** |
| **T4** | status | `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| **T5** | tertinggi | `[80, 60, 90, 70]` | `90` | `0` | **FAIL** |

## Bug Report
* **Bug ID: B01**
  * **Gejala:** Hasil perhitungan rata-rata pada test case T1 dan T2 salah (tidak sesuai ekspektasi).
  * **Test case:** T1, T2
  * **Lokasi:** Fungsi `hitung_rata_rata(nilai)`
  * **Akar penyebab:** Pembagi matematika di-*hardcode* dengan angka tetap `/ 5` padahal jumlah elemen list bersifat dinamis.
  * **Perbaikan:** Mengubah pembagi menjadi `len(nilai)` dan menambahkan pengaman list kosong.
  * **Retest:** PASS

* **Bug ID: B02**
  * **Gejala:** Input nilai `60` pada fungsi status menghasilkan "Tidak lulus" padahal seharusnya "Lulus".
  * **Test case:** T3
  * **Lokasi:** Fungsi `status(nilai)`
  * **Akar penyebab:** Penggunaan operator pembanding yang salah, yaitu menggunakan `> 60` alih-alih `>= 60`.
  * **Perbaikan:** Mengganti kondisi percabangan menjadi `if nilai >= 60:`.
  * **Retest:** PASS

* **Bug ID: B03**
  * **Gejala:** Fungsi pencarian nilai tertinggi selalu mengembalikan angka `0`.
  * **Test case:** T5
  * **Lokasi:** Fungsi `nilai_tertinggi(nilai)`
  * **Akar penyebab:** Inisialisasi awal variabel `tertinggi = 0` dan arah operator pembanding yang salah (`if x < tertinggi`).
  * **Perbaikan:** Mengambil elemen pertama list sebagai inisialisasi awal (`tertinggi = nilai[0]`) dan mengubah operator menjadi `if x > tertinggi`.
  * **Retest:** PASS

## Retest
Seluruh test case dari T1 sampai T5 telah dijalankan kembali setelah perbaikan kode diterapkan. Hasil pengujian menunjukkan seluruh test case kini berstatus **PASS** dan tidak ditemukan adanya regresi pada data valid.

## Cara Menjalankan
```bash
python praktik/praktik_4_debugging.py
python latihan/01_trace_loop.py
python latihan/02_trace_fungsi.py
python latihan/03_test_case.py
python latihan/04_debug_rata_rata.py
``` 
## Refleksi
Teknik debugging yang paling membantu adalah pengujian menggunakan Test Case batas (Boundary Testing) dan pemanfaatan Tracing manual / Debugger. Teknik ini sangat efektif karena mampu membuktikan secara empiris letak penyimpangan alur logika pada baris kode tertentu, sehingga perbaikan dapat diselesaikan secara tepat dan akurat sesuai spesifikasi modul.


