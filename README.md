# 📹 QueueVision AI: Pendeteksi Antrean

## 📖 Deskripsi Proyek
QueueVision AI adalah sebuah aplikasi berbasis visi komputer (Computer Vision) yang dirancang untuk mendeteksi dan menghitung jumlah orang di dalam suatu antrean berdasarkan input gambar dari kamera pengawas (CCTV). Aplikasi ini dibangun menggunakan antarmuka interaktif **Streamlit** dan memanfaatkan arsitektur model *deep learning* **YOLOv8** (You Only Look Once versi 8) untuk melakukan deteksi objek (kepala manusia) secara *real-time* dan akurat. 

Proyek ini bertujuan untuk membantu manajemen fasilitas umum atau ritel dalam memantau kepadatan antrean, sehingga dapat mengambil keputusan lebih cepat seperti menambah staf pelayanan jika antrean terlalu panjang.

## 🎯 Tema yang Dipilih
**Penerapan Kecerdasan Buatan (AI) untuk Analisis Keramaian dan Manajemen Antrean (Crowd Analysis & Queue Management).**

## 📊 Sumber Dataset
Model AI dalam proyek ini dilatih menggunakan **Mall Dataset**. Dataset ini berisi kumpulan frame video dari kamera pengawas (CCTV) di dalam sebuah pusat perbelanjaan, yang sangat cocok untuk kasus deteksi keramaian atau penghitungan kepadatan manusia di area publik.

* **Tautan Dataset:** [Kaggle - Mall Dataset](https://www.kaggle.com/datasets/chaozhuang/mall-dataset?resource=download)

## 🚀 Petunjuk Cara Menjalankan Kode

Berikut adalah langkah-langkah untuk menjalankan aplikasi QueueVision AI di komputer lokal Anda:

### 1. Persiapan Lingkungan (Environment)
Pastikan Anda sudah menginstal **Python** (disarankan versi 3.8 ke atas) di komputer Anda. Disarankan untuk menggunakan *virtual environment* (opsional tapi sangat dianjurkan):
```bash
python -m venv env
# Di Windows
env\Scripts\activate
# Di Mac/Linux
source env/bin/activate
```

### 2. Instalasi Dependensi (Library)
Buka terminal/Command Prompt di direktori proyek ini, lalu jalankan perintah berikut untuk menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt
pip install streamlit
```
*(Catatan: `streamlit` diperlukan untuk menjalankan antarmuka web)*

### 3. Menjalankan Aplikasi
Setelah proses instalasi selesai, jalankan perintah berikut untuk memulai aplikasi web Streamlit:
```bash
streamlit run app.py
```

### 4. Menggunakan Aplikasi
* Setelah menjalankan perintah di atas, browser akan otomatis terbuka (biasanya di `http://localhost:8501`).
* Klik tombol **"Browse files"** untuk mengunggah gambar antrean atau CCTV (format JPG/PNG).
* Sistem akan memproses gambar tersebut menggunakan model YOLOv8.
* Hasil akhir berupa gambar dengan *bounding box* (kotak biru di sekitar kepala orang) dan total jumlah orang akan ditampilkan di layar.
