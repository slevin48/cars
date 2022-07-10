# Copy ✂️ & Paste 📋

import streamlit as st
import clipboard
import pandas as pd

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


st.title("Entry Form 📋")

p = ["url","model","price","mileage","options"]
n = len(p)
b = [None]*n
v = [None]*n
f = [None]*n


for i in range(n):

    # initialisation
    if i not in st.session_state:
        st.session_state[i] = ""

    c1, c2 = st.sidebar.columns(2)

    with c1:
        st.text(p[i])
        b[i] = st.button("📋",key="b"+str(i))
    with c2:
        if b[i]:
            v[i] = clipboard.paste()
            st.session_state[i] = v[i]
        else:
            v[i] = st.session_state[i]
        f[i] = st.text_input("",value = v[i],key="f"+str(i))
    
# st.session_state
df = pd.DataFrame.from_dict({p[i]:f[i] for i in range(n)},orient='index')
st.table(df)

csv = convert_df(df)

st.download_button(
   "download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)