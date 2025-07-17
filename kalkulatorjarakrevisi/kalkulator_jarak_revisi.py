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

    # Visualisasi kotak grid: baris = jam, kolom = km per jam
    fig, ax = plt.subplots(figsize=(kecepatan, waktu))

    for row in range(waktu):
        for col in range(kecepatan):
            ax.add_patch(plt.Rectangle((col, -row-1), 1, 1, edgecolor='black', facecolor='skyblue'))

    ax.set_xlim(0, kecepatan)
    ax.set_ylim(-waktu, 0)

    # ✅ Set xticks dan label sesuai jumlah posisi
    tick_x = np.arange(0, kecepatan + 1, 1)
    tick_y = np.arange(-waktu, 1, 1)

    ax.set_xticks(tick_x)
    ax.set_xticklabels([f"{i} km" for i in tick_x])

    ax.set_yticks(tick_y)
    ax.set_yticklabels([f"{abs(i)} jam" for i in tick_y])

    ax.set_title("Setiap kotak = 1 km | Setiap baris = 1 jam")
    ax.grid(False)
    ax.set_aspect('equal')
    ax.tick_params(left=False, bottom=False)

    st.pyplot(fig)

    st.info(f"""
    📘 **Penjelasan Visual:**
    - Terdapat {waktu} baris → karena kamu berjalan selama {waktu} jam.
    - Setiap baris berisi {kecepatan} kotak → karena tiap jam menempuh {kecepatan} km.
    - Total kotak: **{jarak} km**.
    - 🧠 Apa rumus yang bisa kamu simpulkan dari ini?
    """)
