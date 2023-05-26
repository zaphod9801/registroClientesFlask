# RegistroClientesFlask
This application serves as client registry tool with a simple login as authentication built using Python and Flask. Here you can view your clients list and make edit
operations over them as edit their info, add new clients or delete. You can also filter by city or download your clients as an Excel file:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/356d182d-5933-4c10-91c1-4efb71d02a7f)

You can also do the same CRUD operations for the cities:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/52f3778a-b2c7-4133-ae3f-60c63ba6ed71)
It is important to say that any update that you make here will inmediately appear in your screen. 

Also this app have the requirements to have this three endpoints:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/196c69c1-23ad-4b4c-8680-11ad69a44282)
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/86c6cd52-ac08-4892-803a-4e0590d42d92)

The first endpoint was used to built the login and authentication system, as the requirement, it uses a jwt with extra security like saving it on cookies, 
using secure cookies and using a csfr token, you can see an example here:
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/19e4d1d5-cb8a-42bc-b17e-14f90ae9cce4)
You can view this information in your browser developer tools, in storage section.

The second endpoint was used as get endpoint you can check on the browser after you logged in, you just have to go to localhost:5000/api/user/info and you will
see something like this:

![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/776421a4-4512-4600-8ae3-bb5672f5f042)

The third endpoint was implemented but it is trickier to check, because it is a put endpoint and need the security requirements.
First I recommend you to install something like postman to do this, you can check how to install it here: https://www.postman.com/downloads/

Second, you have to go to modify something in the code, so go inside the app folder and there open the app.py folder. Here you have to change this line to "False":

![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/8293f115-6991-457b-950f-2d0b1bdd55c4)
For default the app blocks any incoming content that use a cookie created in client-side. 
Once you have done this you have to send a request like this:

![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/bf5143ad-9f94-4fd0-883c-f8a56d7c3d92)
![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/8c5aa84e-740c-491d-87fb-1085e6d15d5b)

And now the third endpoint will give you the response:

![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/ca81766e-62fa-4484-b1bd-8f13aef949c8)


## Quickstart Guide
In order to install and run this project you must first clone this repository inside any folder on your personal computer and navigate into that folder. 
Once you have done this, there are two methods to install and run the app, I will explain them as follow:

### Using Docker
This method have as a requisite to have Docker installed on your computer, you can check it out how to it here: https://docs.docker.com/engine/
Once you have Docker installed, you just have to run the following two commands (you MUST run them on the project root folder)

```bash
docker build -t registro-clientes-app .
```
This command will build the docker image of the app with the specifications contained in the Dcokerfile

```bash
docker run -p 5000:5000 registro-clientes-appp
```

This command will run the previously built image, for default it runs on the port 5000 so take it into account, Once you have done this you can go to:
localhost:5000/ and you should saw the app login screen, there you can go to registry screen to register and enter the app.


### Manual usage
You can also install and run the app on your own machine, as a recommendation, you should have installed virtualenv on your machine, you can check out the installation and setup
here: https://virtualenv.pypa.io/en/latest/installation.html
Once you are here, you have to run the following commands on your terminal:
```bash
pip install -r requirements.txt
pip install -e .
```
This commands will install the libraries and dependecies of the project but also the project itself. 

Before running the app, you must run the following command too:
```bash
python app/set_db.py
```
This command will create and populate a sqlite3 database, this is very important for the app usage. 

Now as last step you must create a .env file inside the app folder like this:

![image](https://github.com/zaphod9801/registroClientesFlask/assets/71454879/2c5132ab-3435-44d4-ad60-32662890f45f)

Remember to change the JWT_SECRET_KEY with your desired value

Now you can run the app just doing:
```bash
python app/run.py
```
And again you just have to go to localhost:5000/ and you will see the login screen.

