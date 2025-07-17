import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Visual Jarak", layout="wide")
st.title("🧠 Kalkulator Jarak")

st.markdown("""
Pelajari hubungan **jarak**, **kecepatan**, dan **waktu** melalui visualisasi interaktif.  
Coba nilai yang berbeda, amati hasilnya, dan **temukan sendiri rumusnya**!
""")

# Input nilai kecepatan dan waktu
st.header("1️⃣ Masukkan Nilai")

col1, col2 = st.columns(2)
with col1:
    kecepatan = st.slider("🚗 Kecepatan (km/jam)", min_value=1, max_value=10, value=3, step=1)
with col2:
    waktu = st.slider("⏱️ Waktu (jam)", min_value=1, max_value=10, value=2, step=1)

jarak = kecepatan * waktu

if st.button("🔍 Hitung dan Visualisasikan"):
    with st.spinner("Menghitung..."):
        time.sleep(1)

    st.success(f"📍 Jarak = **{jarak} km**")

    # Visualisasi blok
    st.header("📊 Visualisasi: Blok Jarak per Jam")

    fig, ax = plt.subplots(figsize=(10, 2))

    # Buat visualisasi berupa blok-blok
    x = 0
    for jam in range(1, waktu + 1):
        for k in range(kecepatan):
            ax.bar(x, 1, color='skyblue', edgecolor='black')
            x += 1

    ax.set_xlim(0, max(10, kecepatan * waktu))
    ax.set_ylim(0, 1.5)
    ax.set_yticks([])
    ax.set_xticks(np.arange(0, kecepatan * waktu + 1, kecepatan))
    ax.set_xlabel("Jarak (km)")
    ax.set_title("Setiap blok = 1 km; 1 jam = deretan blok berjumlah kecepatan")
    st.pyplot(fig)

    # Penjelasan eksploratif
    st.info(f"""
    🔎 **Penjelasan Visual:**
    - Setiap baris waktu (jam) berisi {kecepatan} 
    - Total blok: {jarak} → berarti kamu telah menempuh {jarak} km dalam {waktu} jam.
    - Apa rumus yang bisa kamu simpulkan dari ini?
    """)


