import streamlit as st
import pandas as pd


st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days")
option=st.selectbox("Selacet data to view",("Temperature","Sky"))
print(option)
st.subheader(f"{option} for the next {days} days in {place}")
