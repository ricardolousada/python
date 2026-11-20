import streamlit as st
import plotly.express as px

st.title("Wheather Forecast for the next days")

place = st.text_input("Place")

days = st.slider("forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option=st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates_list = ["2022-15-10","2022-15-11","2022-15.12"]
    temperatures = [21,30,40]
    temperatures = [days * i for i in temperatures]
    return dates_list,temperatures

d,t = get_data(days)

figure = px.line(x=d,y=t,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)