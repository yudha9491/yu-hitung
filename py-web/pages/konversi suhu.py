# page1.py
import streamlit as st

st.set_page_config(
    page_title="konversi suhu",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

st.header("konversi Suhu")

temperature = st.number_input("Masukkan nilai suhu", value=1.0)

unit = st.selectbox("Pilih satuan asal", ("Celsius", "Fahrenheit", "Kelvin", "Reamur"))

def convert_temperature(temp, from_unit):
    if from_unit == "Celsius":
        c = temp
        f = (temp * 9/5) + 32
        k = temp + 273.15
        r = temp * 4/5
    elif from_unit == "Fahrenheit":
        c = (temp - 32) * 5/9
        f = temp
        k = (temp + 459.67) * 5/9
        r = (temp - 32) * 4/9
    elif from_unit == "Kelvin":
        c = temp - 273.15
        f = (temp * 9/5) - 459.67
        k = temp
        r = (temp - 273.15) * 4/5
    elif from_unit == "Reamur":
        c = temp * 5/4
        f = (temp * 9/4) + 32
        k = (temp * 5/4) + 273.15
        r = temp
        
    return c, f, k, r

celsius, fahrenheit, kelvin, reamur = convert_temperature(temperature, unit)

st.write("Hasil Konversi:")
st.write(f"Celsius: {celsius:.2f} °C")
st.write(f"Fahrenheit: {fahrenheit:.2f} °F")
st.write(f"Kelvin: {kelvin:.2f} K")
st.write(f"Reamur: {reamur:.2f} °R")
