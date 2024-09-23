import steamlit as st

x =  st.number_input(
    "Insert a namber", value=None, placeholder="Type a number...")
)
st.write("The current number is ", x)
st.latex(r'''
    x^2 = 
    ...)
st.write(x=x)
  
