# iliwycmbd_streamlit
This is the repository for the streamlit presentation.

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
|requirements.txt      | Libraries not included in Streamlit Cloud      |

***

# Streamlit Application Overview & Docuementation
What is [Streamlit?](https://streamlit.io/)
- importable package designed for creating webpages from simple scripts
- uses basic commands to deploy a local webpage with interactive components and other elements from your python code
- this allows us to create our ML model using Python scripts and then deploy it to a shareable webpage

## ML Deployment with Streamlit

#### App development Examples 

[4 Part Series on making and deploying a Streamlit Application](https://www.youtube.com/watch?v=-IM3531b1XU&t=452s&ab_channel=M%C4%B1sraTurp)

## ML Model deployment with Pickling 
[Model Pickling Example & Documentation](https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb)


## Charts & Programming in Streamlit
Streamlit documentation and programming examples can be found [here](https://docs.streamlit.io/)

### Charts

#### Line Charts 

- [Line Chart Documentation](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)

```
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

#### Bar Charts 

- [Bar Chart Documentation](https://docs.streamlit.io/library/api-reference/charts/st.bar_chart)

```
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
```

#### Maps

- [Map Documentation](https://docs.streamlit.io/library/api-reference/charts/st.map)

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
We recommend you use docker for this example, but you usually need Anaconda to run locally.
- [Windows Installation](https://docs.anaconda.com/anaconda/install/windows/)
 
- [Mac OS Installation](https://docs.anaconda.com/anaconda/install/mac-os/)
  
-  [Linux Installation](https://docs.anaconda.com/anaconda/install/linux/)

## Fork and Clone Repository
Fork this repository to your personal Github account.

- Open a new window in VS code
- Click "Clone Git Repository" then "Clone from GitHub"

If it asks for sign-in using GitHub, click "Allow" and "Authorize Visual_Studio_Code". Put in your GitHub password. Then click "Open Visual Studio Code" and it will show your repositories in the search bar. 

Click on your iliwycmbd_streamlit repo and save it to your Big Data folder (where you keep DS460 files). It is crucial to save it in your class folder! This will make everything run smoothly for you today.

## Docker Setup
-  In VS code install the Dev Containers extension.

![image](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/dev_containers.jpg)

#### Windows
Open powershell as an admin.

#### Mac OS
Open docker desktop.
Open a terminal.

### Navigate to your 460 folder in your powershell/terminal directory.
Then copy and paste this code 👇

```
docker pull jupyter/all-spark-notebook
```

Run one of these two options below based on your computer.

#### MacOS/Linux
```
docker run -it -p 8888:8888 -p 8501:8501 -v "${PWD}":/home/jovyan/work jupyter/all-spark-notebook
```

#### Windows
```
docker run -it -p 8888:8888 -p 8501:8501 -v "$(pwd):/home/jovyan/work" jupyter/all-spark-notebook 
```
Use the url to open the allspark notebook.


Go to VS code
- Click green symbol in bottom left corner ("Open a Remote Window").

![image](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/dev_cont_icon_launch.jpg)

- Click "attach to running container", this will show you that container that we ran through docker from powershell. A new window will open in VS code
- Bring in the left side bar, to folders, and click Open folder. Then click ok to load everything in.

Note - In the work folder you will see the iliwycmbd_streamlit folder containing all the files from the original GitHub repo.


Open your terminal

- Run to install streamlit: 
```
pip install streamlit
```

In the work folder through the iliwycmbd_streamlit folder, open the **iris_app.py** file 

Import streamlit using: 

```
import streamlit as st
```

Let's put a title in our app and launch it:

```
st.title("This is my streamlit app")
```
- **Save the file**

In your terminal type the command: 
```
streamlit run "work/iliwycmbd_streamlit/iris_app.py"
```
- Ctrl/Cmd click the External URL to launch to a browser

If this does not work for you, try putting this in the searchbar of your browser to go directly to your file: localhost:8501


Continue to edit and save the file, and all we have to do is refresh the streamlit tab in our browser for it to update!


Let's try this by adding a streamlit write statement to our code:
```
st.write("Adding more to my app")
```
- save the file, and go to your streamlit webpage and refresh the page. You should see your changes there.

## 2 Fork Repo

iliwycmbd_streamlit Repository - 
[iliwycmbd_streamlit Repo Link](https://github.com/byuibigdata/iliwycmbd_streamlit)


## 2.1 Clone Repo

Clone the repository to your computer and make sure to save the file in your DS460 Folder or where your docker Container is. This will allow you to work on the files within your docker enviroment. 

## 3 Pickle iris_ml.py 

In order to be able to deploy a machine learning model in an application for real world use, it will need to be saved into a file that can be deployed. This example uses the method of pickling to make a model deployable. The code to facilitate this process is very simple and will be demonstrated in the following code chunk. The library needs to be imported first to be able to pickle the model. Then the function $pickle.dump()$ can be called to save the model. In the first term of the function that needs to be specified is the model that needs to be pickled. The next term that needs to be specified in the name of the .pkl that the model will be saved to. 

```
import pickle

pickle.dump(model, open('model.pkl', 'wb'))
```

This will create a .pkl file that can be called to use the model where it is being deployed. In this example the pickled file will be used to demonstrate model deployment using a streamlit app to make the model usbale either in an organization or publicly.

Start by trying to pickle the **iris_ml_model.py** file found within the iliwycmbd_streamlit folder. If any issues are encounterd attempting to pickle this model plesae refer to **iris_ml_example.py**. This file has the model pickled within it. Please note that to continue on with the Streamlit example this file needs to pickled. 



## Develop Streamlit app on iris_app.py 

If there are any questions, feel free to reference the completed steamlit app example file found here:

[Iris Streamlit App Example](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/iris_app_example.py)

## Deploy app Locally while in Devlopment 

This is how to deploy a local streamlit app for use during app development. In this deployment it will only be accesible on the computer that it was deployed on. It is useful to verify how the app currently looks and to view any changes made. It is also benficial to view any changes before pushing to github/production.  

- Navigate working directory to app file location through PowerShell/terminal
- Example code: 
```
cd Desktop
```
- run the following code 👇
```
streamlit run app_name.py
```
- Copy & Paste URL if needed
- Re-Run when code is updated to verify changes
- Set re-run to automatic to update when file is saved


## Publishing App on Streamlit Cloud

This section will cover how to publish an app to streamlit cloud. This is very useful for making a dashboard avaliable for internal use within an orginization or for releasing a dashboard for public use.

The first step in publishing an app with streamlit is to make sure that the necessary files have been uploaded to right github repositriy. If that has not been done, be sure to do that now. 

IF you are calling any libraries that are not included in a standard pytohn file, a text file called "requirements" will need to be added to your file directory or repository. Simply create a text file and add the desired libraries to the file followed by a "-dev". The folloiwing is an example of what you would do with the pandas library. 

```
pandas-dev
```

After the files that are going to be published are pushed to github, it is time to log into streamlit. If an account needs to be created please use the following link. 

```
https://share.streamlit.io/signup
```

This is an example of this app published on the streamlit cloud app:
[Iris_Example_App](https://byuibigdata-iliwycmbd-streamlit-iris-app-example-u6z8lb.streamlit.app/)


After logging in please navigate to the home page. This will look like the image below. To deploy a new app begin by selecting the button titled "New app". This button is highlighted in the image below. 

![create_project](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/creat_new_app.png)

After clicking the buttom to create a new app you will be directed to this page. This is where you will naviage through your github account to find the app that you want to publish and select the desired pyton file. After the file is selected all you need to do is hit delpoy and your app will launch shortly!

![image](https://github.com/byuibigdata/iliwycmbd_streamlit/blob/main/Publish%20on%20Streamlit%20Cloud/select_github_location.png)
