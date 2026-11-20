import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Hapiness")

x_axis = st.selectbox(label="Select the data for the X-axis",options=("GDP","generosity","happiness"))
print(x_axis)

y_axis = st.selectbox(label="Select the data for the Y-axis",options=("GDP","generosity","happiness"))
print(y_axis)

df = pd.read_csv("happy.csv")

d = df[x_axis.lower()]
t = df[y_axis.lower()]

figure = px.scatter(x=d,y=t,
                 labels={"x": x_axis, "y":y_axis},)
st.plotly_chart(figure)