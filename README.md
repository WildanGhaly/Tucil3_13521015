
# Tugas Kecil III - Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer

## Deskripsi Tugas
Algoritma UCS (Uniform cost search) dan A* (atau A star) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan lintasan terpendek berdasarkan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan (simpang 3, 4 atau 5) atau ujung jalan. Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara lainnya yang disediakan oleh Google Map.
Langkah pertama di dalam program ini adalah membuat graf yang merepresentasikan peta (di area tertentu, misalnya di sekitar Bandung Utara/Dago). Berdasarkan graf yang dibentuk, lalu program menerima input simpul asal dan simpul tujuan, lalu menentukan lintasan terpendek antara keduanya menggunakan algoritma UCS dan A*. Lintasan terpendek dapat ditampilkan pada peta/graf (misalnya jalan-jalan yang menyatakan lintasan terpendek diberi warna merah). Nilai heuristik yang dipakai adalah jarak garis lurus dari suatu titik ke tujuan. 
Spesifikasi program:
1.	Program menerima input file graf (direpresentasikan sebagai matriks ketetanggaan berbobot), jumlah simpul minimal 8 buah.
2.	Program dapat menampilkan peta/graf
3.	Program menerima input simpul asal dan simpul tujuan.
4.	Program dapat menampilkan lintasan terpendek beserta jaraknya antara simpul asal dan simpul tujuan.
5.	Antarmuka program bebas, apakah pakai GUI atau command line saja.

## Requirement dan Cara Menjalankan Program

Program ini menggunakan bahasa Python sehingga hanya akan bisa dijalankan apabila sistem telah memiliki instalasi Python. Program juga memanfaatkan beberapa library berikut yang mungkin perlu diinstall:

```bash
  math
  PyQt5
  sys
  folium
```

Setelah itu program akan bisa dijalankan dengan cara menjalankan kode berikut:

```bash
  cd src
  python main.py
```
## Authors

- 13521015 [Hidayatullah Wildan Ghaly Buchary](https://github.com/WildanGhaly)

