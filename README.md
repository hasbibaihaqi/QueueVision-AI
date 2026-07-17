# 📹 QueueVision AI: Sistem Pendeteksi & Penghitung Antrean Otomatis

QueueVision AI adalah sistem berbasis Computer Vision yang dirancang untuk mendeteksi pengunjung dan menghitung jumlah antrean secara real-time dari tangkapan kamera CCTV. Proyek ini menggunakan algoritma **YOLOv8** untuk deteksi objek (kepala manusia) dan dikemas ke dalam aplikasi web interaktif menggunakan **Streamlit**.

---

## 🚀 Fitur Utama
* **Deteksi Kepala Pengunjung (Object Detection):** Akurat mendeteksi kerumunan atau antrean manusia menggunakan model YOLOv8 kustom.
* **Penghitung Otomatis (Real-time Counter):** Menghitung total orang yang berada di dalam antrean secara otomatis dan menampilkannya langsung pada layar.
* **Web Interface Ringan:** Antarmuka berbasis web yang interaktif dan mudah digunakan menggunakan Streamlit, memungkinkan pengguna mengunggah gambar untuk dianalisis secara instan.

---

## 🛠️ Tech Stack & Library
* **Bahasa Pemrograman:** Python 3.14+
* **Framework AI:** Ultralytics YOLOv8
* **Pemrosesan Gambar & Video:** OpenCV, Matplotlib
* **Antarmuka Web (Deployment):** Streamlit
* **Eksperimen Lingkungan:** Jupyter Notebook

---

## 📁 Struktur Proyek
```text
QueueVision AI/
│
├── data/                    # Dataset gambar dan video antrean (diabaikan di git)
├── models/                  # Menyimpan bobot model terbaik (best.pt)
├── notebooks/               # File eksperimen (.ipynb) dari Tahap 1 - 3
│   ├── 01_preprocessing.ipynb
│   ├── 02_training_baseline.ipynb
│   └── 03_evaluation_comparison.ipynb
├── src/                     # Kode sumber aplikasi (Data loader, Trainer, Utils)
├── app.py                   # File utama aplikasi web Streamlit
├── .gitignore               # Daftar pembatas file upload Git
└── README.md                # Dokumentasi proyek (File ini)
