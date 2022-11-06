# iliwycmbd_streamlit
This is the repository for the streamlit presentation.

***

## ML Deployment with Streamlit

- What stream is

- What it allowed us to do


- Finished Titanic ML app 

## ML Model deployment with Pickling 
[Model Pickling Example & Docuementation](https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb)


## Charts & Programming in Streamlit
Streamlit docuementation and programing examples can be found here
- [Streamlit Docuementation](https://docs.streamlit.io/)

### Charts

#### Line Charts 

- [Line Chart Docuementation](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

#### Bar Charts 

- [Bar Chart Docuementation](https://docs.streamlit.io/library/api-reference/charts/st.bar_chart)

```
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
```

#### Maps

- [Map Chart Docuementation](https://docs.streamlit.io/library/api-reference/charts/st.map)

```
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
```
### UI Programing


***

#  Docuementation for Iris Streamlit ML App

## Anaconda Installation 
- [Windows Installation](https://docs.anaconda.com/anaconda/install/windows/)
 
- [Mac OS Installation](https://docs.anaconda.com/anaconda/install/mac-os/)
  
-  [Linuix Installation](https://docs.anaconda.com/anaconda/install/linux/)

## Fork Repo

iliwycmbd_streamlit Reposistory - 
[iliwycmbd_streamlit Repo Link](https://github.com/byuibigdata/iliwycmbd_streamlit)

## Pickle iris_ml.py 

In order to be able to deploy a machine learning model in an application for real world use, it will need to be saved into a file that can be deployed. This example uses the method of pickling to make a model deployable. The code to facilitate this process is very simple and will be demonstrated in the following code chunk. The library needs to be imported first to be able to pickle the model. Then the function $pickle.dump()$ can be called to save the model. In the first term of the function that needs to be specified is the model that needs to be pickled. The next term that needs to be specified in the name of the .pkl that the model will be saved to. 

```
import pickle

pickle.dump(model, open('model.pkl', 'wb'))
```

This will create a .pkl file that can be called to use the model where it is being deployed. In this example the pickled file will be used to demonstrate model deployment using a streamlit app to make the model usbale either in an organization or publicly.

Start by trying to pickle the iris_ml_model.py file found within the iliwycmbd_streamlit folder. If any issues are encounterd attempting to pickle this model plesae refer to the iris_ml_example.py file. This file has the model pickled within it. Please note that to continue on with the Streamlit example this file needs to pickled. 



## Develop Streamlit app on iris_app.py 

If there are any questions, feel free to reference the completed steamlit app example file found here:

[Iris Streamlit App Example](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/iris_app_example.py)

## Deploy app Locally whil in Devlopment 

- Naviget working directory to app file location
- run the following code 

```
streamlit run app_name.py
```
- Copy & Paste URL if needed
- Re-Run when code is updated to verify changes
- Set re-run to automatic to update when file is saved
        

## Publishing App on Streamlit Cloud

This section will cover how to publish an app to streamlit cloud. This is very useful for making a dashboard avaliable for internal use within an orginization or for releasing a dashboard for public use.

The first step in publishing an app with streamlit is to make sure that the necessary files have been uploaded to right github repositriy. If that has not been done, be sure to do that now. 

After the files that are going to be published are pushed to github, it is time to log into streamlit. If an account needs to be created please use the following link. 

```
https://share.streamlit.io/signup
```

After logging in please navigate to the home page. This will look like the image below. To deploy a new app begin by selecting the button titled "New app". This button is highlighted in the image below. 

![create_project](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/creat_new_app.png)

After clicking the buttom to create a new app you will be directed to this page. This is where you will naviage through your github account to find the app that you want to publish and select the desired pyton file. After the file is selected all you need to do is hit delpoy and your app will launch shortly!

![image](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/select_github_location.png)
