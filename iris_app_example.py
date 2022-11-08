import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
import pickle

iris = pd.read_csv('/Users/luskenterprises/Downloads/iris_csv.csv')


X = iris.loc[:, iris.columns != 'class']
Y = iris.loc[:, iris.columns == 'class']


st.sidebar.header('Specify Input Parameters')

def user_input_features():
    sepallength = st.sidebar.slider('sepallength', 0.1,8.1,4.0, step=.1)
    sepalwidth = st.sidebar.slider('sepalwidth', 0.1,8.1,4.0, step=.1)
    petallength = st.sidebar.slider('petallength',0.1,2.1,1.1, step=.1)
    petalwidth = st.sidebar.slider('petalwidth', 0.1,2.1,1.1, step=.1)
    data ={'sepallength':sepallength,
            'sepalwidth':sepalwidth,
            'petalwidth':petalwidth,
            'petallength':petallength
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

load_clf = pickle.load(open('irirs_model.pkl', 'rb'))

prediction = prediction[0]

st.header('Specified Input parameters')
st.write(df)
st.write('---')

st.header('Prediction of Flower Type')
st.write(prediction)
st.write('---')

f = prediction

if f == "Setosa":
    setosa = st.image("images/setosa.jpg", caption = "Iris Setosa", width = 350)
elif f == "Virginica":
    virginica = st.image("images/virginica.jpg", caption = "Iris Virginica", width = 350)
elif f == "Versicolor":
    versicolor = st.image("images/versicolor2.jpg", caption = "Iris Versicolor", width = 350)

