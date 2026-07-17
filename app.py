import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# Mengatur tampilan halaman web
st.set_page_config(page_title="QueueVision AI Demo", layout="centered")
st.title("📹 QueueVision AI: Pendeteksi Antrean")
st.write("Unggah gambar dari CCTV untuk mendeteksi dan menghitung jumlah orang di dalam antrean.")

# Memuat model AI (disimpan di cache agar web tidak lemot saat di-refresh)
@st.cache_resource
def load_model():
    return YOLO('models/baseline/weights/best.pt')

model = load_model()

# Membuat tombol unggah gambar
uploaded_file = st.file_uploader("Pilih gambar antrean (Format JPG/PNG)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.write("Sedang menganalisis...")
    
    # 1. Mengubah file unggahan menjadi format gambar yang bisa dibaca OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # 2. Menyuruh AI mendeteksi kepala orang
    results = model.predict(image, conf=0.25)
    
    # 3. MENGHITUNG TOTAL ORANG (Saran ke-2)
    total_orang = len(results[0].boxes)
    
    # 4. Menggambar kotak biru dari YOLO
    res_image = results[0].plot()
    
    # 5. MENAMBAHKAN TEKS PENGHITUNG ALA CCTV (Saran ke-2)
    # Teks hijau menyala di pojok kiri atas (koordinat 30, 50)
    cv2.putText(res_image, f"TOTAL ANTREAN: {total_orang} ORANG", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3, cv2.LINE_AA)
    
    # 6. Menyesuaikan warna gambar agar tidak kebiruan di halaman Web (BGR ke RGB)
    res_image_rgb = cv2.cvtColor(res_image, cv2.COLOR_BGR2RGB)
    
    # Menampilkan hasilnya ke layar web Anda
    st.success(f"Analisis selesai! Terdeteksi {total_orang} orang.")
    st.image(res_image_rgb, caption="Hasil Deteksi QueueVision AI", use_container_width=True)