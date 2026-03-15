======= Setup ========
uvicorn <filename>:<fastapi_object> --reload
source /venv/bin/activate

1. To change env to venv -> source /venv/bin/activate

2. To run the backend server -> uvicorn <filename>:<fastapi_object> --reload
--reload means that reload the sever whene changes observerd

3. 

==========Dynamic Routing==========
There are three input types. They are

===path parameter===
@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message":f"hello {name}"}

===query parameter ===
@app.get("/hello")
def say_hello(limit:int,page:int):
    return {"message":f"{limit},{page}"}

=== request body ===
class User(BaseModel):
    name: str
    age : int
    email : str | None = None # Here None = None means email is not required attribute. it is not mandatory
    bank_balance : int = 0 # here =0 after datatype means that if user didnt give this attribute take 0 as default

@app.post("/users")
def create_user(user : User):
    return{
        "Message":"User successfully created",
        "user":user
    }


Dynamic routing:
1. In main.py see that in curly brackets a variable is declared. It is dynamic routing. That means we can get usernames from there for example.
2. After making a route dynamic, to get the variable we need to chech if it is of required datatype.
3. We need to pass that variable as functions parameter.


===========BaseModel===============

from pydantic import BaseModel   #BaseModel is used to check Data type and also type convertion.


class User(BaseModel):
    name: str
    age : int

@app.post("/users")
def create_user(user : User):
    return{
        "Message":"User successfully created",
        "user":user
    }
1. In the above snippet BaseModel is imported from pydantic. It is used to check datatype and also used for typecasting.
2. It converts json object into python object and validates the datatypes


==== methods ====
# Always Look from user perspective. i.e. client
1. post-> It is used to post something to server
2. get-> It is used to get something from server
3. put-> It is used to update something in server
4. 

=======routes,APIRouter======
1. As creating more end points makes main file clumsey, we create a folder for routes and import them in main file.
2. To do so we need APIRouter from fastapi. look over the syntax. 
3. We jsut create instance of the class APIRouter and upload all routes to that instance, finally we import this file intlo main file and use it by using app.include_router()
