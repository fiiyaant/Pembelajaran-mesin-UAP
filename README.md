# 🌲 Analisis Sentimen Ulasan Wisata Alam untuk Meningkatkan Pengalaman Pengunjung 🌿

![Wisata Alam](https://www.google.com/url?sa=i&url=https%3A%2F%2Fkemenparekraf.go.id%2Fragam-pariwisata%2FDestinasi-Wisata-Indonesia-Jadi-Tempat-Liburan-Pesohor-Dunia&psig=AOvVaw3-8R5dF2yoI-RE3n0Pvg2Z&ust=1735265155325000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjfi_qsxIoDFQAAAAAdAAAAABAE)


---
## **Table of Contents**
- [About](#about)
- [Dataset](#dataset)
- [Installation](#Installation)
- [Model Description](#Model-Description)
- [Result](#Result)
- [web](#web)
- [Anggota Tim](#anggota-tim)

---
## About

Proyek ini bertujuan untuk menganalisis sentimen dari ulasan wisata alam yang diberikan oleh pengunjung. Dengan memahami pola sentimen dari ulasan ini, diharapkan dapat:
- Membantu pengelola wisata memperbaiki layanan berdasarkan umpan balik pengunjung.
- Meningkatkan pengalaman pengunjung secara keseluruhan.
- Menggunakan model deep learning seperti LSTM dan GRU untuk memberikan prediksi sentimen yang akurat.

---
**Fitur Utama Aplikasi:**

- Prediksi Sentimen: Mengelompokkan ulasan ke dalam kategori positif, netral, atau negatif.
- Visualisasi Hasil: Menampilkan distribusi probabilitas hasil prediksi.
= Model Interaktif: Pilih antara model LSTM atau GRU untuk prediksi.
---

## 📊Dataset

**Deskripsi Dataset:**
Dataset berisi ulasan wisata alam yang mencakup beberapa kolom:
- **Text:** Ulasan pengunjung.
- **Rating:** Sentimen pengunjung dalam skala 1-5.
- **Aspek Lain:** Seperti fasilitas, aktivitas, dan aksesibilitas.

| **Kolom**       | **Deskripsi**                           |
|------------------|-----------------------------------------|
| `text`          | Ulasan wisata alam dari pengunjung.     |
| `rating`        | Skor sentimen dalam skala 1-5.         |
| `facility`      | Aspek fasilitas wisata.                |
| `accessibility` | Tingkat aksesibilitas ke lokasi.       |

---
## ⚙️Installation

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di lokal Anda:
**1.Clone Repository**

```
git clone https://github.com/fiiyaant/Pembelajaran-mesin-UAP.git
cd Pembelajaran-mesin-UAP
```
**2. Install Dependencies Gunakan file requirements.txt untuk menginstal semua**

- Depedencies:
```
pip install -r requirements.txt
```
**3.Run Application Jalankan aplikasi Streamlit:**
```
streamlit run app.py
```
---
## 🧠 Model Description
Proyek ini menggunakan dua model utama untuk analisis sentimen:

**1.LSTM (Long Short-Term Memory):**
- Arsitektur:
- Embedding Layer
  - LSTM Layers (128 dan 64 unit)
  - Dense Layer (32 unit, ReLU)
  - Output Layer (5 kelas, Softmax)
- Akurasi: 65%
- F1-Score Kelas Mayoritas: 0.79

**2.GRU (Gated Recurrent Unit):**
- rsitektur:
- Embedding Layer
    - GRU Layers (128 dan 64 unit)
    - Dense Layer (32 unit, ReLU)
    - Output Layer (5 kelas, Softmax)
- Akurasi: 65%
- F1-Score Kelas Mayoritas: 0.79
---
## 📈  Results

**LSTM**
| Kelas | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 1     | 0.00      | 0.00   | 0.00     | 38      |
| 2     | 0.00      | 0.00   | 0.00     | 35      |
| 3     | 0.00      | 0.00   | 0.00     | 176     |
| 4     | 0.00      | 0.00   | 0.00     | 559     |
| 5     | 0.65      | 1.00   | 0.79     | 1516    |
- Analisis:
  - Model memiliki performa yang baik untuk kelas mayoritas (kelas 5) dengan nilai Recall sebesar 1.00 (artinya semua sampel kelas 5 berhasil diklasifikasikan).
  - Namun, performa pada kelas minoritas (kelas 1, 2, 3, dan 4) sangat buruk dengan nilai Precision dan Recall sebesar 0.00. Hal ini menunjukkan bahwa model cenderung bias terhadap kelas mayoritas.
  - Kesimpulan: Model cenderung mengalami masalah class imbalance, di mana kelas mayoritas mendominasi hasil prediksi, sedangkan kelas minoritas terabaikan.

**GRU**
| Kelas | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 1     | 0.00      | 0.00   | 0.00     | 38      |
| 2     | 0.00      | 0.00   | 0.00     | 35      |
| 3     | 0.00      | 0.00   | 0.00     | 176     |
| 4     | 0.50      | 0.00   | 0.00     | 559     |
| 5     | 0.65      | 1.00   | 0.79     | 1516    |
- Analisis:
  - Sama seperti LSTM, model GRU juga menunjukkan performa yang baik pada kelas mayoritas (kelas 5) dengan nilai Recall sebesar 1.00.
  - Performanya sedikit lebih baik pada kelas 4 dibandingkan dengan LSTM, dengan nilai     Precision sebesar 0.50, meskipun nilai Recall tetap rendah.
  - Namun, untuk kelas minoritas lainnya (kelas 1, 2, dan 3), model tidak mampu memberikan  prediksi yang baik (Precision dan Recall sebesar 0.00).
  - Kesimpulan: Sama seperti LSTM, model GRU juga mengalami masalah class imbalance, meskipun       sedikit lebih baik dalam menangani kelas minoritas tertentu (kelas 4).
---
🌐 Web
Web ini memiliki antarmuka web interaktif yang memungkinkan pengguna memasukkan ulasan wisata dan memilih model untuk prediksi. Berikut adalah cuplikan aplikasi web:
![image](https://github.com/user-attachments/assets/d820d40b-07f2-495d-aabd-4da54654fabd)

**Notes**
Web ini dirancang untuk memudahkan pengguna yang ingin menganalisis sentimen ulasan wisata tanpa memerlukan pengetahuan teknis. Pengguna hanya perlu memasukkan ulasan wisata dan memilih model yang ingin digunakan, lalu aplikasi akan memberikan hasil prediksi secara real-time.
Berikut fitur utama dari tampilan web ini:
  - Pilihan Model Prediksi: Pengguna dapat memilih antara model LSTM atau GRU untuk melakukan analisis sentimen.
  - Masukan Teks Ulasan: Pengguna dapat memasukkan ulasan wisata mereka ke dalam kotak teks yang telah disediakan.
  -Tombol Prediksi Sentimen: Dengan sekali klik tombol, hasil prediksi sentimen akan langsung ditampilkan.
  - Hasil Prediksi dan Visualisasi: Prediksi sentimen ditampilkan dengan penjelasan singkat, dilengkapi dengan visualisasi probabilitas setiap kategori sentimen.
---
 **ampilan Input dan Pilihan Model**   
![Image2](https://github.com/fiiyaant/Pembelajaran-mesin-UAP/blob/ae05f41a0a417c7a6d631a457edbecd32b333248/image/image2.png?raw=true)

---

**Prediksi Sentimen dan Distribusi Probabilitas**
![Image3](https://github.com/fiiyaant/Pembelajaran-mesin-UAP/blob/ae05f41a0a417c7a6d631a457edbecd32b333248/image/image3.png?raw=true)

---

Aplikasi web ini dapat diakses melalui tautan berikut:  [Sentimen Wisata](https://pembelajaran-mesin-uap-peytahnxjtvvavckoe8xdc.streamlit.app/)

---

---
## Penyusun

- **Nama:** Nur Fitri Yanti
- **Nim:** 202110370311088
