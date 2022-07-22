import streamlit as st

st.write('''
# Max of the 3 numbers

This app finds the max of the 3 number entered by the user''')

x1 = float(st.number_input("First Number"))
x2 = float(st.number_input("Second Number"))
x3 = float(st.number_input("Third Number"))

st.subheader('Answer')
st.write('Max number =', max(x1,x2,x3))
