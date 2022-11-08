# iliwycmbd_streamlit
This is the repository for the streamlit presentation.

### Docuement Summary 



### Repository File Dictionary 

| File Name            |Description                                     |
|----------------------|------------------------------------------------|
|README.md             | Overview and Streamlit Docuemnetation.         |
|irirs_model.pkl       | The Pickled ML Model for the Iris Dataset      | 
|iris.csv.             | The Dataset in csv format                      | 
|iris_app.py           | A partily complete copy of the app to work on  |                
|iris_app_example.py   | The finished Streamlit App                     |                
|iris_ml_example.ipynb | The Complete ML Model with Pickling Code       |
|iris_ml_model.ipynb   | The Not Complete Iris ML Model - Needs Piclking|
***

# Streamlit Application Overview & Docuementation

## ML Deployment with Streamlit

- What stream is

- What it allowed us to do

- Finished Titanic ML app 

#### App development Examples 

[4 Part Series on making and deploying a Streamlit Application](https://www.youtube.com/watch?v=-IM3531b1XU&t=452s&ab_channel=M%C4%B1sraTurp)

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

#  

## Anaconda Installation 
- [Windows Installation](https://docs.anaconda.com/anaconda/install/windows/)
 
- [Mac OS Installation](https://docs.anaconda.com/anaconda/install/mac-os/)
  
-  [Linuix Installation](https://docs.anaconda.com/anaconda/install/linux/)

## Docker Setup
-  In VS code install the Dev Containers extension.

Notes From Docker Presentation:
Navigate to the directory you want to use your notebook in.
In a command prompt (or terminal) run docker pull jupyter/all-spark-notebook
Run: docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/all-spark-notebook (MacOS/Linux)
Run: docker run -it --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" jupyter/all-spark-notebook (Windows)
The -it flag instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container. I remeber this as 'integrated terminal'.

The --rm flag automatically removes the container when it exits.

The -p 8888:8888 flag is telling docker to bind the port 8888 of the container to you local port 8888.

The -v flag mounts the current working directory into the container. We are telling it to mount "${PWD}" (which gets our current directory) into the notebooks /home/jovyan/work directory. This allows the container to save the work being done in the container to a local directory as well.

If you close a server after working and then come back and start a new server your previous work should still be there because of the -v flag.

All of this can also be done from the Docker Desktop app. You can also remove the --rm command if you do not want the container to be cleared after every run.


- Take out the --rm
- Add after 8888:8888 -p 8501:8501 (May be a different port for others)
- Run the docker run code to open the allspark notebook

- Go to VS code
- Click bottom >< thing from dev container extension.
- Click attach to running container, this should show you that container that we ran from Docker groups code, click that and you will be taken to a new vs code window with all those files.
- Open your terminal (you can press ctrl j to do this as well)
- run this code to install streamlit: pip install streamlit
- create a python file in the work folder called streamlit.py
- In that file write this code to import streamlit: import streamlit as st
- Let's put a title to our app and launch it. Write the code: st.title("This is my dope streamlit app")
- Save the file
- In your terminal type the command: streamlit run "work/streamlit.py"
- ctrl click the External URL, this will launch your app into your web browser.
- If this does not work for you, you may need to go to it directly to it by putting this in your searchbar: localhost:8501 (May be a different port for others)


Now we can continually edit and save our streamlit.py file and all we have to do is refresh the tab in our browser for it to update!
Let's try this by adding a streamlit write statement to our code: st.write("Does this actually work?")

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

This is how to deploy a local streamlit app for use during app development. In this deployment it will only be accesible on the computer that it was deployed on. It is useful to verify how th app currently looks and to view any changes made. It is also benficial after an app is deployed to view any changes before pushing to github/production.  

- Naviget working directory to app file location through terminal
- Example code: 
```
cd Desktop
```
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
