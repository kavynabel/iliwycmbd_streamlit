# iliwycmbd_streamlit
This is the repository for the streamlit presentation.

***

## ML Deployment with Streamlit

- What stream is

- What it allowed us to do


- Finished Titanic ML app 

## Streamlit through Docker
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


## ML Model deployment with Pickling 

## Charts & Programming in Streamlit

## Docuementation for Titanic Streamlit ML App

- Anaconda Installation 
 Windows - https://docs.anaconda.com/anaconda/install/windows/
 Mac OS - https://docs.anaconda.com/anaconda/install/mac-os/
 Linuix - https://docs.anaconda.com/anaconda/install/linux/

- Fork Repo

- Pickle titanic_ml.py 

- Develop Streamlit app on titanic_app.py 

- Deploy app on Streamlit cloud

## Publishing App on Streamlit Cloud
