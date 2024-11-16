import streamlit as st

st.set_page_config(
    page_title="kalkulator",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")
st.title("Kalkulator ")

num1 = st.number_input("Masukkan angka pertama", value=0.0)
num2 = st.number_input("Masukkan angka kedua", value=0.0)


operation = st.selectbox("Pilih operasi", ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"))


if operation == "Penjumlahan":
    result = num1 + num2
elif operation == "Pengurangan":
    result = num1 - num2
elif operation == "Perkalian":
    result = num1 * num2
elif operation == "Pembagian":
    result = num1 / num2 if num2 != 0 else "Tidak dapat dibagi dengan nol"

st.write("Hasil:", result)
