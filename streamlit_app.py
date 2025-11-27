import streamlit as st
import time

st.title("⏳ Timer Sederhana dengan Streamlit")

# Input durasi timer (dalam detik)
duration = st.number_input("Masukkan durasi timer (detik):", min_value=1, value=10)

# Tombol mulai
if st.button("Mulai Timer"):
    st.write("Timer dimulai...")
    placeholder = st.empty()

    for remaining in range(duration, 0, -1):
        placeholder.markdown(f"## ⏰ Waktu tersisa: **{remaining} detik**")
        time.sleep(1)

    placeholder.markdown("## ✔️ Timer selesai!")
