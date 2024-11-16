import streamlit as st


def set_page(page_name):
    st.session_state["page"] = page_name

st.set_page_config(
    page_title="Yu Hitung",
    page_icon="🧮",
)

st.sidebar.info("pilih jenis operasi diatas")

st.write("""
# Selamat Datang!
website ini menyediakan berbagai macam jenis perhitungan
untuk memudahkan perhitungan mu!
""")

st.write("""
support saya untuk mengembangkan website ini!
""")

st.write("""
[instagram](https://www.instagram.com/yu_code___/)
""")
