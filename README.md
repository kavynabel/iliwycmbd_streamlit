# iliwycmbd_streamlit
This is the repository for the streamlit presentation.

***

## ML Deployment with Streamlit

- What stream is

- What it allowed us to do


- Finished Titanic ML app 

## ML Model deployment with Pickling 

## Charts & Programming in Streamlit

#  Docuementation for Titanic Streamlit ML App

## Anaconda Installation <br>
              - Windows - https://docs.anaconda.com/anaconda/install/windows/ <br>
              - Mac OS - https://docs.anaconda.com/anaconda/install/mac-os/ <br>
              - Linuix - https://docs.anaconda.com/anaconda/install/linux/ <br>

## Fork Repo

## Pickle iris_ml.py 

In order to be able to deploy a machine learning model in an application for real world use, it will need to be saved into a file that can be deployed. This example uses the method of pickling to make a model deployable. The code to facilitate this process is very simple and will be demonstrated in the following code chunk. The library needs to be imported first to be able to pickle the model. Then the function $pickle.dump()$ can be called to save the model. In the first term of the function that needs to be specified is the model that needs to be pickled. The next term that needs to be specified in the name of the .pkl that the model will be saved to. 

```
import pickle

pickle.dump(model, open('model.pkl', 'wb'))
```

This will create a .pkl file that can be called to use the model where it is being deployed. In this example the pickled file will be used to demonstrate model deployment using a streamlit app to make the model usbale either in an organization or publicly.

Start by trying to pickle the iris_ml_model.py file found within the iliwycmbd_streamlit folder. If any issues are encounterd attempting to pickle this model plesae refer to the iris_ml_example.py file. This file has the model pickled within it. Please note that to continue on with the Streamlit example this file needs to pickled. 



## Develop Streamlit app on titanic_app.py 

## Deploy app on Streamlit cloud

## Publishing App on Streamlit Cloud



![create_project](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/creat_new_app.png)



![image](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/select_github_location.png)
