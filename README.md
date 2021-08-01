# PROPERTY API INTEGRATION


## Technologies:
 1. Django
 2. Django-rest-framework
 3. Python
 4. Sqlite

## Usage
Only dev enviroment is avaliable, current project have 3 endpoints you can find the postman collection inside the project.
For using you must install your own pyenv with requeriments on file requierements.txt
After you install everything and djnango is running as a server , you can test the following endpoints
   
   Database data 
   **user: inna 
   password:12345**
You can create another user in the database if you want it.

## Features
 1.  POST -> *http://127.0.0.1:8000/properties/*
 Get all properties avaliable on system with status pre_sold, available and sold; you can send parameters inside the body request if you want some specific information about properties.
 *Authentication is not needed. 
 
 *Body*
  

      { "city":"Tunja",
    
    "state":"Boyaca",
    
    "year":"2000"}

 2.  POST -> *http://127.0.0.1:8000/authenticator/*
Generate token autenticator for next petition
 *Authentication is not needed. 
 
 *Body*
  

      { "username":"inna",
    
    "password":"12345"}

 2.  POST -> *http://127.0.0.1:8000/like/*
Save relation between user and property. Save authenticated user related to property_id sent on body of request
 *Authentication is required
 
 *Body*
  

      { "property_id":1 }
## Postman Collection

**habitest.postman_collection.json**
#### Author
Innacroft
[Link to My portfolio](https://innacroft.github.io/portfolio/)<br>
![](https://github.com/innacroft/portfolio/blob/gh-pages/images/back_inna.png)



