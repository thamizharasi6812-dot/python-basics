import streamlit as st

def add_num(a,b):
    return a+b

#add_num()
st.title("calculator")
num1=st.text_input("first number:")
num2=st.text_input("second number:")
if st.button("add"):
    result=add_num(int(num1),int(num2))
    st.write(f"result:{result}")