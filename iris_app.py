# Import packages
import pandas as pd
import pickle
import altair as alt

''' Make title'''


''' Streamlit Write Command'''


'''Load Data rename columns '''

#iris = pd.read_csv('https://raw.githubusercontent.com/byuibigdata/iliwycmbd_streamlit/main/iris.csv')

#iris = iris.rename(columns={'sepal.length': 'sepallength', 'sepal.width': 'sepalwidth', 'petal.length': 'petallength', 'petal.width': 'petalwidth'})

''' For the ml model dedicate which columns will be your feature under 'X' and our target under 'Y'''

#X = iris.loc[:, iris.columns != 'variety']
#Y = iris.loc[:, iris.columns == 'variety']


# add a subheader explaining what the ml model will do


''' Add a title for your sidebar '''

# st.sidebar.header('Specify Input Parameters')


''' bellow is the code to add sliders and to connect them to a dataset which we will use for our ml model. Add a slider for sepal length'''
#def user_input_features():
 #   sepalwidth = st.sidebar.slider('Sepal Width', 0.1,8.1,4.0, step=.1)
  #  petallength = st.sidebar.slider('Petal Length',0.1,2.1,1.1, step=.1)
   # petalwidth = st.sidebar.slider('Petal Width', 0.1,2.1,1.1, step=.1)
    #data ={ 'sepalwidth':sepalwidth,
     #       'petalwidth':petalwidth,
      #      'petallength':petallength
    #}
    #features = pd.DataFrame(data, index=[0])
    #return features

#df = user_input_features()


''' load pickel with our ml model'''

#load_clf = pickle.load(open('work/iliwycmbd_streamlit/irirs_model.pkl', 'rb'))

''' load prediction and prediction probability '''

#prediction = load_clf.predict(df)
#prediction_proba = load_clf.predict_proba(df)
#prediction = prediction[0]

''' display the data that the user inputed and display the prediction '''



''' add any charts, visuals or widgets that you would like '''

