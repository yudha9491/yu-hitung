
import streamlit as st

st.set_page_config(
    page_title="hitung tekanan hidrostatis",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

st.title("Kalkulator Tekanan Hidrostatis")
st.write("""
    Tekanan Hidrostatis adalah tekanan yang dialami oleh suatu benda yang berada di dalam fluida (seperti air) akibat pengaruh gravitasi pada kolom fluida di atasnya. Tekanan ini meningkat seiring dengan bertambahnya kedalaman, karena semakin dalam posisi benda, semakin besar massa fluida di atasnya yang memberikan tekanan ke bawah. Konsep ini penting dalam berbagai bidang, seperti kedokteran, teknik sipil, dan geologi, karena tekanan hidrostatis mempengaruhi benda-benda yang terbenam di bawah permukaan air.

Rumus tekanan hidrostatis:


P=ρ⋅g⋅h 
di mana:


P adalah tekanan hidrostatis (Pa atau N/m²),


ρ adalah massa jenis fluida (kg/m³),


g adalah percepatan gravitasi (m/s²), biasanya sekitar 

9,8m/s 
2
 ,

 h adalah kedalaman atau jarak vertikal dari permukaan fluida ke titik yang diukur (m).
""")

operation = st.selectbox("Pilih apa yang ingin dicari", ("tekanan(p)", "massa jenis fluida(kg/m³)", "kedalaman(m)"))


if operation == "tekanan(p)":
    rho = st.number_input("Masukkan massa jenis fluida (kg/m³):", min_value=0.0, step=0.1)
    depth = st.number_input("Masukkan kedalaman atau tinggi kolom fluida (m):", min_value=0.0, step=0.1)
    gravity = st.number_input("Masukkan percepatan gravitasi (m/s²):", value=9.8, step=0.1)

    
    result = rho*depth*gravity
    st.write("Hasil:", result, "N/m²")

elif operation == "massa jenis fluida(kg/m³)":
    depth = st.number_input("Masukkan kedalaman atau tinggi kolom fluida (m):", min_value=0.0, step=0.1)
    preasure = st.number_input("Masukkan tekanan(N/m²):", min_value=0.0, step=0.1)
    gravity = st.number_input("Masukkan percepatan gravitasi (m/s²):", value=9.8, step=0.1)

    result = preasure/(depth*gravity)
    st.write("Hasil: ", result, "kg/m³")

elif operation == "kedalaman(m)":
    preasure = st.number_input("Masukkan tekanan(N/m²):", min_value=0.0, step=0.1)
    gravity = st.number_input("Masukkan percepatan gravitasi (m/s²):", value=9.8, step=0.1)
    rho = st.number_input("Masukkan massa jenis fluida (kg/m³):", min_value=0.0, step=0.1)

    result = preasure/(rho*gravity)
    st.write("Hasil: ", result, "m")
