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

    # Set 1 kotak mewakili 10 km
    km_per_kotak = 10
    kotak_per_baris = max(1, kecepatan // km_per_kotak)  # minimal 1 agar tidak error
    total_kotak = kotak_per_baris * waktu

    fig, ax = plt.subplots(figsize=(kotak_per_baris, waktu))  # Ukuran lebih proporsional

    # Gambar kotak
    for row in range(waktu):
        for col in range(kotak_per_baris):
            ax.add_patch(
                plt.Rectangle((col, -row), 1, -1, edgecolor='black', facecolor='skyblue')
            )

    ax.set_xlim(0, kotak_per_baris)
    ax.set_ylim(-waktu, 0)

    # Label sumbu x
    x_ticks = np.arange(0, kotak_per_baris, 1)
    x_labels = [f"{(i+1)*km_per_kotak} km" for i in x_ticks]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)

    # Label sumbu y
    y_ticks = np.arange(0, -waktu, -1)
    y_labels = [f"{abs(i)} jam" for i in y_ticks]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)

    ax.set_title("Setiap kotak = 10 km | Baris = 1 jam", fontsize=12)
    ax.grid(False)
    ax.set_aspect('equal')
    ax.tick_params(left=False, bottom=False)

    st.pyplot(fig)

    st.info(f"""
    📘 **Penjelasan Visual:**
    - Setiap **baris** menunjukkan waktu 1 jam.
    - Dalam 1 jam, kamu menempuh {kecepatan} km → jadi 1 baris = {kotak_per_baris} kotak (1 kotak = 10 km).
