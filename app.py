import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer dan model
tokenizer = joblib.load("tokenizer.joblib")  # Pastikan file ini ada di folder proyek
model_lstm = load_model("lstm.h5")  # Pastikan file ini ada di folder proyek
model_gru = load_model("gru.h5")  # Pastikan file ini ada di folder proyek

# Fungsi preprocessing teks
def preprocess_text(text):
    import re
    text = re.sub(r"http\S+|www.\S+", "", text)  # Hilangkan URL
    text = re.sub(r"\d+", "", text)  # Hilangkan angka
    text = re.sub(r"[^\w\s]", "", text)  # Hilangkan tanda baca
    text = text.strip()  # Trim spasi
    return text

# Fungsi prediksi
def predict_sentiment(model, text, tokenizer, max_len=100):
    # Preprocessing teks
    cleaned_text = preprocess_text(text)
    
    # Tokenisasi dan padding
    tokenized_text = tokenizer.texts_to_sequences([cleaned_text])
    padded_text = pad_sequences(tokenized_text, maxlen=max_len, padding='post')
    
    # Prediksi
    prediction = model.predict(padded_text)
    predicted_class = np.argmax(prediction) + 1  # Tambahkan 1 agar sesuai kelas 1-5
    return predicted_class, prediction

# Streamlit UI
# Custom Theme
st.set_page_config(
    page_title="Sentimen Wisata",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Header
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        color: #3A7D44;
        text-align: center;
    }
    .description {
        color: #555;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Analisis Sentimen Ulasan Wisata Alam 🌄</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Aplikasi ini menggunakan model AI (LSTM dan GRU) untuk menganalisis sentimen ulasan wisata.</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Pengaturan Aplikasi")
st.sidebar.write("Pilih model untuk prediksi:")
model_choice = st.sidebar.radio("Model Prediksi", ["LSTM", "GRU"], index=0)

st.sidebar.markdown("### Tips:")
st.sidebar.info(
    """
    - Masukkan ulasan wisata Anda di bawah.
    - Pilih model untuk analisis.
    - Klik tombol **Prediksi** untuk melihat hasil.
    """
)

# Input dari pengguna
st.markdown("<h2 style='color: #3A7D44;'>Masukkan Ulasan Anda:</h2>", unsafe_allow_html=True)
text_input = st.text_area("", placeholder="Tulis ulasan wisata Anda di sini...", height=150)

# Tombol prediksi
if st.button("Prediksi Sentimen 🧠"):
    if text_input.strip() == "":
        st.error("Harap masukkan ulasan sebelum prediksi!")
    else:
        # Pilih model
        model = model_lstm if model_choice == "LSTM" else model_gru
        
        # Prediksi
        predicted_class, prediction = predict_sentiment(model, text_input, tokenizer)
        
        # Hasil prediksi
        st.markdown("<h2 style='color: #3A7D44;'>Hasil Prediksi:</h2>", unsafe_allow_html=True)
        st.success(f"Prediksi Sentimen: **Kelas {predicted_class}**")
        
        # Visualisasi probabilitas
        st.markdown("<h3 style='color: #3A7D44;'>Distribusi Probabilitas:</h3>", unsafe_allow_html=True)
        st.bar_chart(prediction[0])

# Footer
st.markdown(
    """
    <hr style='border:1px solid #3A7D44;'>
    <p style='text-align: center; color: #555;'>Dikembangkan oleh Tim Analisis Sentimen Wisata © 2023</p>
    """,
    unsafe_allow_html=True
)
