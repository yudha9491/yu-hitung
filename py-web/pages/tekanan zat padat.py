import streamlit as st

st.set_page_config(
    page_title="hitung tekanan zat padat",
    page_icon="🧮",
)


st.sidebar.info("pilih jenis operasi diatas")

st.title("tekanan zat padat")

st.write("""
    Tekanan pada Zat Padat adalah gaya yang bekerja pada suatu permukaan per satuan luas. Dalam konteks zat padat, tekanan ini terjadi ketika gaya diberikan pada suatu permukaan benda padat, seperti saat seseorang berdiri di atas tanah atau sebuah objek diletakkan di atas meja. Tekanan ini dapat dihitung dengan membagi gaya yang bekerja dengan luas permukaan tempat gaya tersebut diterapkan.

Rumus tekanan pada zat padat adalah:

P= F/A
​
 
di mana:


P adalah tekanan (Pa atau N/m²),


F adalah gaya yang bekerja tegak lurus pada permukaan (N),


A adalah luas permukaan yang dikenai gaya (m²). 

""")

operation = st.selectbox("Pilih apa yang ingin dicari", ("tekanan(p)", "Gaya(F)", "luas bidang(A)"))


if operation == "tekanan(p)":
    F = st.number_input("masukan gaya (N):", value=1.0)
    A = st.number_input("Masukan luas bidang:", value=1.0)

    result = F / A
    if st.button("Hitung tekanan"):
        st.write("Hasil:", result, "Pa")

elif operation == "Gaya(F)":
    A = st.number_input("Masukan luas bidang:")
    P = st.number_input("Masukan tekanan (Pa):")
    result = A*P
    if st.button("Hitung Gaya"):
        st.write("Hasil: ", result, "N")

elif operation == "luas bidang(A)":
    F = st.number_input("masukan gaya (N):")
    P = st.number_input("Masukan tekanan (Pa):")
    result = F*P
    if st.button("Hitung luas bidang"):
        st.write("Hasil: ", result, "m3")


