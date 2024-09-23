import streamlit as st

x =  st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write ("Anda masukkan", x,' ',sx)
sy = st.text_input("Dikonversi ke", "F", "K", "R")
y = 0
if (sx == 'C'):
  if (sy == 'C'):
    y=x
  elif(sy == 'F'):
    (9/5) * x + 32
  elif(sy == 'K'):
    x+273.15
  elif(sy == 'R'):
    x*0.8
st.write (x,'',sx,'=...', sy)

  
