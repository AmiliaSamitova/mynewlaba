import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("titanic.csv")

st.title('Данные пассажиров Титаника')
st.subheader('Описательная статистика')
st.write(titanic.describe())
st.write('Столбцы и их типы:')
st.write(titanic.dtypes)
st.write('Форма таблицы:', titanic.shape)

#пользователь может выставить определнное количество строк таблицы, по умолчанию 5 
num_rows = st.number_input('Количество строк:', min_value=1, max_value=len(titanic), value=5)
st.write(titanic.head(num_rows))

st.subheader('Графики')
#гистограмма распределения возрастов
st.subheader('Распределение возрастов пассажиров')
sns.histplot(titanic['Age'].dropna(), bins=30) #dropna() удаляет пропуски
st.pyplot()
