# RegistroClientesFlask
This application serves as client registry tool with a simple login as authentication built using Python and Flask. Here you can view your clients list and make edit
operations over them as edit their info, add new clients or delete. You can also filter by city or download your clients as an Excel file:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/356d182d-5933-4c10-91c1-4efb71d02a7f)

You can also do the same CRUD operations for the cities:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/52f3778a-b2c7-4133-ae3f-60c63ba6ed71)
It is important to say that any update that you make here will inmediately appear in your screen. 

## Quickstart Guide
In order to install and run this project you must first clone this repository inside any folder on your personal computer and navigate into that folder. 
Once you have done this, there are two methods to install and run the app, I will explain them as follow:

### Using Docker
This method have as a requisite to have Docker installed on your computer, you can check it out how to it here: https://docs.docker.com/engine/
Once you have Docker installed, you just have to run the following two commands (you MUST run them on the project root folder)

```console
docker build -t registro-clientes-app .
```
This command will build the docker image of the app with the specifications contained in the Dcokerfile

```console
docker run -p 5000:5000 registro-clientes-appp
```

This command will run the previously built image, for default it runs on the port 5000 so take it into account, Once you have done this you can go to:
localhost:5000/ and you should saw the app login screen, there you can go to registry screen to register and enter the app.


### Manual usage
You can also install and run the app on your own machine, as a recommendation, you should have installed virtualenv on your machine, you can check out the installation and setup
here: https://virtualenv.pypa.io/en/latest/installation.html
Once you are here, you have to run the following commands on your terminal:
```console
pip install -r requirements.txt
pip install -e .
```
This commands will install the libraries and dependecies of the project but also the project itself. 

Before running the app, you must run the following command too:
```console
python app/setDB.py
```
This command will create and populate a sqlite3 database, this is very important for the app usage. 

Now you can run the app just doing:
```console
python app/run.py
```
And again you just have to go to localhost:5000/ and you will see the login screen.

