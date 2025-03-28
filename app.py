import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if 'page' not in st.session_state:
    st.session_state.page = 'home'

titanic = pd.read_csv("titanic.csv")

def home_page():

    st.title('Данные пассажиров Титаника')
    st.subheader('Описательная статистика')
    st.write(titanic.describe())
    st.write('Столбцы и их типы:')
    st.write(titanic.dtypes)
    st.write('Форма таблицы:', titanic.shape)

    #пользователь может выставить определенное количество строк таблицы, по умолчанию 5 
    num_rows = st.number_input('Количество строк:', min_value=1, max_value=len(titanic), value=5)
    st.write(titanic.head(num_rows))
    if st.button('Перейти на страницу 2'):
        st.session_state.page = 'page2'

def page2():
    st.subheader('Графики')

    #строим гистограммы в зависимости от параметра,который выбирает пользователь
    choice = st.selectbox('Выберите класс:',['pclass', 'sex', 'Age', 'embarked'] )
    st.subheader(f'Распределение людей на Титанике по параметру {choice}')
    if choice == 'pclass':
        plt.figure(figsize=(10, 5))
        sns.histplot(titanic['Pclass'].dropna(), bins=30) 
        st.pyplot(plt.gcf())
    elif choice == 'sex':
        plt.figure(figsize=(10, 5))
        sns.histplot(titanic['Sex'].dropna(), bins=30) 
        st.pyplot(plt.gcf())
    elif choice == 'Age':
        plt.figure(figsize=(10, 5))
        sns.histplot(titanic['Age'].dropna(), bins=30) 
        st.pyplot(plt.gcf())
    else:
        plt.figure(figsize=(10, 5))
        sns.histplot(titanic['Embarked'].dropna(), bins=30) 
        plt.legend(title="Порты", labels=['Southampton, Cherbourg, Queenstown' ])
        st.pyplot(plt.gcf())
    
    



    #график выживаемости по полу
    plt.figure(figsize=(10, 5))
    st.subheader('Выживаемость в зависимости от пола')
    sns.countplot(x='Sex', hue='Survived', data=titanic) #hue позволяет отобразить данные разных категорий в легенде
    st.pyplot(plt.gcf()) #возвращает текущую фигуру, созданную с помощью библиотеки Matplotlib

    #график выживаемости по возрасту
    plt.figure(figsize=(40, 20))
    st.subheader('Выживаемость в зависимости от возраста')
    sns.countplot(x='Age', hue='Survived', data=titanic) 
    st.pyplot(plt.gcf())

    #график выживаемости по классу
    plt.figure(figsize=(10, 5))
    st.subheader('Выживаемость в зависимости от класса')
    sns.countplot(x='Pclass', hue='Survived', data=titanic) 
    st.pyplot(plt.gcf())

    #диаграмма круговая количеств различных классов
    plt.figure(figsize=(10, 5))
    st.subheader('Распределение по Ticket class')
    class_counts = titanic['Pclass'].value_counts()
    plt.pie(class_counts, labels=class_counts.index)
    plt.axis('equal')  # Сделать круговой график кругом
    st.pyplot(plt.gcf())

    #график, отображающий среднюю стоимость билетов по классам
    plt.figure(figsize=(8, 6))
    average_fare = titanic.groupby('Pclass')['Fare'].mean()
    average_fare.plot(kind='line')
    plt.title('Средняя стоимость билета по классам на Титанике')
    plt.xlabel('Класс')
    plt.ylabel('Средняя стоимость')

    plt.tight_layout()
    st.pyplot(plt.gcf())

    if st.button('Вернуться на главную'):
        st.session_state.page = 'home'

if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'page2':
    page2()

