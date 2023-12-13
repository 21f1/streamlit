import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

st.title('Find the largest number (Created for TDS by 21F1000512)')

num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')

if st.button('Find Largest'):
    result = find_largest(num1, num2, num3)
    st.write(f'The largest number is {result}')
