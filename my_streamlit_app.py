import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover stremalit possibilities, let's enjoy")

import streamlit as st

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")