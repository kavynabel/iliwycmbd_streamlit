# Import packages


# Load data & rename columns 

iris = pd.read_csv('https://raw.githubusercontent.com/byuibigdata/iliwycmbd_streamlit/main/iris.csv')

iris = iris.rename(columns={'sepal.length': 'sepallength', 'sepal.width': 'sepalwidth', 'petal.length': 'petallength', 'petal.width': 'petalwidth'})

# For the ml model dedicate which columns will be your feature under 'X' and our target under 'Y'
X = 
Y = 

# Add a title to your app, shortcuts included in the links given under Header.


# add a subheader explaining what the ml model will do


# add a title for your sidebar


# Below is the code to add sliders and to connect them to a dataset which we will use for our ml model
# Add a slider for sepal length 
def user_input_features():
    sepalwidth = st.sidebar.slider('Sepal Width', 0.1,8.1,4.0, step=.1)
    petallength = st.sidebar.slider('Petal Length',0.1,2.1,1.1, step=.1)
    petalwidth = st.sidebar.slider('Petal Width', 0.1,2.1,1.1, step=.1)
    data ={ 'sepalwidth':sepalwidth,
            'petalwidth':petalwidth,
            'petallength':petallength
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


# Load the pickled ML model

load_clf = pickle.load(open('load pickle here', 'rb'))

# Load prediction & prediction probability 
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

# Display the data that the user inputed and display the prediction


# Add any charts, visuals or widgets that you would like 


