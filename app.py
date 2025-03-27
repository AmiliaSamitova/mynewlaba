import streamlit as st
import pandas as pd

titanic = pd.read_csv("titanic.csv")

st.title('Данные пассажиров Титаника')
st.subheader('Описательная статистика')
st.write(titanic.describe())
st.write('Столбцы и их типы:')
st.write(titanic.dtypes)
st.write('Форма таблицы:', titanic.shape)
