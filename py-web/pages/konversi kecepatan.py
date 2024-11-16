import streamlit as st

st.set_page_config(
    page_title="konversi kecepatan",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

st.header("Konversi Kecepatan")
    
speed = st.number_input("Masukkan nilai kecepatan", value=0.0)
speed_unit = st.selectbox("Pilih satuan asal kecepatan", ("km/jam", "m/detik", "mil/jam", "knot"))
    
def convert_speed(value, from_unit):
    if from_unit == "km/jam":
        kmh = value
        ms = value / 3.6
        mph = value / 1.609
        knot = value / 1.852
    elif from_unit == "m/detik":
        kmh = value * 3.6
        ms = value
        mph = value * 2.237
        knot = value * 1.944
    elif from_unit == "mil/jam":
        kmh = value * 1.609
        ms = value / 2.237
        mph = value
        knot = value / 1.151
    elif from_unit == "knot":
        kmh = value * 1.852
        ms = value / 1.944
        mph = value * 1.151
        knot = value

    return kmh, ms, mph, knot

kmh, ms, mph, knot = convert_speed(speed, speed_unit)
    
st.write("Hasil Konversi Kecepatan:")
st.write(f"Kilometer per jam: {kmh:.2f} km/jam")
st.write(f"Meter per detik: {ms:.2f} m/detik")
st.write(f"Miles per jam: {mph:.2f} mil/jam")
st.write(f"Knot: {knot:.2f} knot")