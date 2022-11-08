import streamlit as st
import pandas as pd
# import shap
import matplotlib.pyplot as plt
from sklearn import datasets
import pickle
import numpy as np


iris = pd.read_csv('https://raw.githubusercontent.com/byuibigdata/iliwycmbd_streamlit/main/iris.csv')

iris = iris.rename(columns={'sepal.length': 'sepallength', 'sepal.width': 'sepalwidth', 'petal.length': 'petallength', 'petal.width': 'petalwidth'})

X = iris.loc[:, iris.columns != 'variety']
Y = iris.loc[:, iris.columns == 'variety']


st.sidebar.header('Specify Input Parameters')

def user_input_features():
    sepallength = st.sidebar.slider('Sepal Length', 0.1,8.1,4.0, step=.1)
    sepalwidth = st.sidebar.slider('Sepal Width', 0.1,8.1,4.0, step=.1)
    petallength = st.sidebar.slider('Petal Length',0.1,2.1,1.1, step=.1)
    petalwidth = st.sidebar.slider('Petal Width', 0.1,2.1,1.1, step=.1)
    data ={'sepallength':sepallength,
            'sepalwidth':sepalwidth,
            'petalwidth':petalwidth,
            'petallength':petallength
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

load_clf = pickle.load(open('work/iliwycmbd_streamlit/irirs_model.pkl', 'rb'))

prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


prediction = prediction[0]


st.header('Specified Input parameters')
st.write(df)
st.write('---')

st.header('Prediction of Flower Type')
st.write(prediction)
st.write('---')


f = prediction

if f == "Setosa":
    setosa = st.image("work/iliwycmbd_streamlit/images/setosa.jpg", caption = "Iris Setosa", width = 350)
elif f == "Virginica":
    virginica = st.image("work/iliwycmbd_streamlit/images/virginica.jpg", caption = "Iris Virginica", width = 350)
elif f == "Versicolor":
    versicolor = st.image("work/iliwycmbd_streamlit/images/versicolor2.jpg", caption = "Iris Versicolor", width = 350)

st.subheader('Prediction Probability')
st.write(prediction_proba)
