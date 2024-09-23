import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan (C, F, K, R)", "C")

sy = st.text_input("Dikonversi ke (C, F, K, R)", "Masukkan satuan")

y = 0

if sx == 'C':  # Celsius
    if sy == 'C':
        y = x
    elif sy == 'F':  # Celsius to Fahrenheit
        y = (9/5) * x + 32
    elif sy == 'K':  # Celsius to Kelvin
        y = x + 273.15
    elif sy == 'R':  # Celsius to Réaumur
        y = x * 4/5
elif sx == 'F':  # Fahrenheit
    if sy == 'C':  # Fahrenheit to Celsius
        y = (x - 32) * 5/9
    elif sy == 'F':
        y = x
    elif sy == 'K':  # Fahrenheit to Kelvin
        y = (x - 32) * 5/9 + 273.15
    elif sy == 'R':  # Fahrenheit to Réaumur
        y = (x - 32) * 4/9
elif sx == 'K':  # Kelvin
    if sy == 'C':  # Kelvin to Celsius
        y = x - 273.15
    elif sy == 'F':  # Kelvin to Fahrenheit
        y = (x - 273.15) * 9/5 + 32
    elif sy == 'K':
        y = x
    elif sy == 'R':  # Kelvin to Réaumur
        y = (x - 273.15) * 0.8
elif sx == 'R':  # Réaumur
    if sy == 'C':  # Réaumur to Celsius
        y = x / 0.8
    elif sy == 'F':  # Réaumur to Fahrenheit
        y = (x * 9/4) + 32
    elif sy == 'K':  # Réaumur to Kelvin
        y = (x / 0.8) + 273.15
    elif sy == 'R':
        y = x

st.write(x, sx, "=", y, sy)
