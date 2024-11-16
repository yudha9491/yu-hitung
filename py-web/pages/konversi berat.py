import streamlit as st

st.set_page_config(
    page_title="konversi berat",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

st.header("Konversi berat")

weight = st.number_input("Masukkan nilai berat", value=0.0)
weight_unit = st.selectbox("Pilih satuan asal berat", ("Kilogram", "Gram", "Pound", "Ons"))
    
def convert_weight(value, from_unit):
    if from_unit == "Kilogram":
        kg = value
        g = value * 1000
        lb = value * 2.205
        oz = value * 35.274
    elif from_unit == "Gram":
        kg = value / 1000
        g = value
        lb = value / 453.592
        oz = value / 28.35
    elif from_unit == "Pound":
        kg = value / 2.205
        g = value * 453.592
        lb = value
        oz = value * 16
    elif from_unit == "Ons":
        kg = value / 35.274
        g = value * 28.35
        lb = value / 16
        oz = value

    return kg, g, lb, oz

kg, g, lb, oz = convert_weight(weight, weight_unit)

st.write("Hasil Konversi Berat:")
st.write(f"Kilogram: {kg:.2f} kg")
st.write(f"Gram: {g:.2f} g")
st.write(f"Pound: {lb:.2f} lb")
st.write(f"Ons: {oz:.2f} oz")