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
Pseudocode:

   Program ini dimulai dengan inisialisasi data berupa sekumpulan angka (nums), nilai target, serta list kosong untuk menyimpan elemen yang dipilih (selected). Sistem kemudian menampilkan antarmuka GUI yang terdiri dari input angka, input target, tombol kontrol, serta area visualisasi berupa canvas. Pengguna dapat menambahkan angka ke dalam sistem melalui input yang tersedia, dan angka tersebut akan ditampilkan secara visual. Selain itu, sistem menyediakan fungsi untuk mereset seluruh data dan tampilan agar dapat digunakan kembali.
   Proses utama dalam algoritma ini terletak pada fungsi rekursif subset_sum yang menerima parameter indeks dan jumlah sementara (current_sum). Pada setiap langkah, algoritma akan memeriksa apakah jumlah sementara sudah sama dengan target, yang menandakan solusi telah ditemukan. Jika indeks telah mencapai batas akhir atau jumlah melebihi target, maka proses dihentikan pada cabang tersebut. Jika kondisi tersebut belum terpenuhi, algoritma akan mengambil elemen pada indeks saat ini, menambahkannya ke dalam subset, dan melanjutkan pencarian secara rekursif ke indeks berikutnya. Proses ini divisualisasikan melalui pembaruan tampilan GUI seperti perubahan warna elemen dan informasi status.
   Apabila langkah tersebut tidak menghasilkan solusi, maka algoritma akan melakukan proses backtracking dengan cara menghapus elemen terakhir yang telah dipilih dari subset. Setelah itu, algoritma akan mencoba kemungkinan lain, yaitu tidak memilih elemen tersebut dan melanjutkan pencarian ke indeks berikutnya. Proses ini akan terus berulang hingga ditemukan kombinasi yang sesuai atau seluruh kemungkinan telah dieksplorasi. Setelah proses selesai, sistem akan menampilkan hasil berupa solusi jika ditemukan, atau informasi bahwa tidak terdapat kombinasi yang memenuhi target.
