import steamlit as st

x =  st.number_input(
    "14", value=None, placeholder="Type a number...")
)
st.write("14", x)
st.latex(r'''
    x^2 = 
    ...)
st.write(x*x)
  
