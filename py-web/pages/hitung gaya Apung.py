import streamlit as st

st.set_page_config(
    page_title="hitung gaya apung",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")


st.title("Kalkulator Gaya Apung")

st.write("""
    Gaya Apung adalah gaya ke atas yang dialami oleh benda ketika diletakkan dalam fluida (cairan atau gas), seperti air atau udara. Gaya ini disebabkan oleh perbedaan tekanan fluida pada bagian atas dan bawah benda tersebut. Prinsip Archimedes menjelaskan bahwa besar gaya apung pada sebuah benda yang tenggelam sebagian atau seluruhnya dalam fluida adalah sama dengan berat fluida yang dipindahkan oleh benda tersebut.

Rumus gaya apung:

𝐹
apung
=

F 
apung 
​
  =ρ⋅V⋅g

di mana:

𝐹
apung 

​
  adalah gaya apung (N),
 𝜌
 adalah massa jenis fluida (kg/m³), 
 𝑉
 adalah volume benda yang tercelup (m³), 

 𝑔
 adalah percepatan gravitasi (m/s²), biasanya sekitar 

9,8m/s 
2
 .
""")

rho = st.number_input("Masukkan massa jenis fluida (kg/m³):", min_value=0.0, step=0.1)

volume = st.number_input("Masukkan volume benda yang tercelup (m³):", min_value=0.0, step=0.1)

gravity = st.number_input("Masukkan percepatan gravitasi (m/s²):", value=9.8, step=0.1)

if st.button("Hitung Gaya Apung"):
    gaya_apung = rho * volume * gravity
    st.write(f"Gaya Apung = {gaya_apung:.2f} N")
