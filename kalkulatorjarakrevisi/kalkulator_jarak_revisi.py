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
    kecepatan = st.slider("🚗 Kecepatan (km/jam)", min_value=1, max_value=200, value=60, step=1)
with col2:
    waktu = st.slider("⏱️ Waktu (jam)", min_value=1, max_value=10, value=2, step=1)

jarak = kecepatan * waktu

if st.button("🔍 Hitung dan Visualisasikan"):
    with st.spinner("Menghitung..."):
        time.sleep(1)

    st.success(f"📍 Jarak = **{jarak} km**")

    # Visualisasi blok: 1 kotak = 10 km (agar efisien)
    kotak_per_baris = kecepatan // 10
    total_kotak = kotak_per_baris * waktu

    fig, ax = plt.subplots(figsize=(12, 5))

    for row in range(waktu):
        for col in range(kotak_per_baris):
            ax.add_patch(
                plt.Rectangle((col, -row), 1, -1, edgecolor='black', facecolor='skyblue')
            )

    ax.set_xlim(0, max(kotak_per_baris, 10))
    ax.set_ylim(-waktu, 0)

    ax.set_xticks(np.arange(0, kotak_per_baris + 1, 1))
    ax.set_xticklabels([f"{(i+1)*10} km" for i in range(kotak_per_baris)])
    ax.set_yticks(np.arange(0, -waktu - 1, -1))
    ax.set_yticklabels([f"{abs(i)} jam" for i in range(0, -waktu, -1)])

    ax.set_title("Setiap kotak = 10 km | Baris = 1 jam")
    ax.grid(False)
    ax.set_aspect('auto')
    ax.tick_params(left=False, bottom=False)

    st.pyplot(fig)

    st.info(f"""
    📘 **Penjelasan Visual:**
    - Setiap **baris** menunjukkan perjalanan selama 1 jam.
    - Dalam 1 jam, kamu menempuh {kecepatan} km → jadi setiap baris punya {kotak_per_baris} kotak (1 kotak = 10 km).
    - Total kotak: {total_kotak} → total jarak = {jarak} km.
    - 🧠 Apa rumus yang bisa kamu simpulkan?
    """)
