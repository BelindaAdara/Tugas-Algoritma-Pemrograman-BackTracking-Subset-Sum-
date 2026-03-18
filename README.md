Berikut versi yang sudah disesuaikan untuk kamu (Subset Sum) dengan format yang sama persis seperti contoh:

---

# Visualisasi Algoritma Backtracking: Subset Sum Solver

Repositori ini berisi *source code* dan dokumentasi untuk pemenuhan Tugas Individu mata kuliah terkait implementasi algoritma Backtracking. Kasus yang dipilih untuk divisualisasikan adalah penyelesaian masalah *Subset Sum*.

**Informasi Mahasiswa:**

* **Nama:** Belinda Adara Putri Aditya
* **NIM:** 21120124140164
* **Kelas/Mata Kuliah:** Algoritma & Pemrograman (C)

---

## 1. Deskripsi Program

Program ini merupakan implementasi dari algoritma Backtracking yang dibuat menggunakan bahasa pemrograman Python. Algoritma Backtracking adalah teknik untuk mencari solusi dari suatu permasalahan secara incremental (satu per satu) dan meng-eliminasi solusi yang tidak sesuai dengan kondisi batasan (*constraint*) yang ditentukan.

Visualisasi dibuat menggunakan GUI (*Graphical User Interface*) berbasis pustaka bawaan Python, yaitu `tkinter`. Program akan mendemonstrasikan bagaimana algoritma secara rekursif memilih elemen dari suatu himpunan, menghitung total sementara, dan melakukan proses *backtrack* (mundur dan menghapus pilihan) ketika jumlah yang diperoleh tidak sesuai atau melebihi target yang ditentukan.

### Batasan (Constraint) Subset Sum:

Program secara ketat mematuhi aturan berikut:

* Input berupa sekumpulan bilangan (list/array).
* Terdapat nilai target yang harus dicapai.
* Setiap elemen hanya dapat digunakan satu kali dalam satu kombinasi.
* Kombinasi yang dipilih harus memiliki jumlah total sama dengan nilai target.

---

## 2. Cara Menjalankan Program

Pastikan Python sudah terinstal di sistem Anda. Pustaka `tkinter` umumnya sudah terinstal secara *default* bersama Python.

1. *Clone* repositori ini atau *download* file `subset_sum_gui.py`.
2. Buka terminal atau *command prompt* di direktori penyimpanan file.
3. Jalankan perintah berikut:

   ```bash
   python subset_sum_gui.py
   ```
