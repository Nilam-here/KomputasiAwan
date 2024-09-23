import streamlit as st

x =  st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write ("Anda masukkan", x,' ',sx)
sy = st.text_input("Dikonversi ke", "F")
y = 0
if (sx == 'C'):
  if (sy == 'C'):
    y=x
  elif(sy == 'F'):
    (9/5) * x + 32
if (sx == 'C'):
  if (sy == 'C'):
    y=x
    elif(sy == 'K'):
      C+273.15
st.write (x,'',sx,'=...', sy)

  
