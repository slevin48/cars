# Copy ✂️ & Paste 📋

import streamlit as st
import clipboard

st.title("Entry Form 📋")

c1, c2 = st.sidebar.columns(2)

with c1:
    st.text("Text1")
    b1 = st.button("📋")
with c2:
    if b1:
        v1 = clipboard.paste()
    else:
        v1 = ""
    f1 = st.text_input("",value = v1)