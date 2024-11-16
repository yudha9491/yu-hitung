import streamlit as st

st.set_page_config(
    page_title="konversi jarak",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

def convert_distance(value, from_unit, to_unit):
    if from_unit == "Meter":
        value_in_meters = value
    elif from_unit == "Kilometer":
        value_in_meters = value * 1000
    elif from_unit == "Mil":
        value_in_meters = value * 1609.34
    elif from_unit == "Kaki":
        value_in_meters = value * 0.3048

    if to_unit == "Meter":
        return value_in_meters
    elif to_unit == "Kilometer":
        return value_in_meters / 1000
    elif to_unit == "Mil":
        return value_in_meters / 1609.34
    elif to_unit == "Kaki":
        return value_in_meters / 0.3048


st.title("Alat Pengonversi Jarak")

distance = st.number_input("Masukkan jarak yang ingin dikonversi:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Dari Satuan:", ["Meter", "Kilometer", "Mil", "Kaki"])
to_unit = st.selectbox("Ke Satuan:", ["Meter", "Kilometer", "Mil", "Kaki"])

if st.button("Konversi"):
    result = convert_distance(distance, from_unit, to_unit)
    st.write(f"Hasil: {distance} {from_unit} = {result:.4f} {to_unit}")