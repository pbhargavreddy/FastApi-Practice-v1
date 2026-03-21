from fastapi import FastAPI,Response,status 
from app.routers import users,posts,inputTypes
from pydantic import BaseModel   #BaseModel is used to check Data type and also type convertion.


app = FastAPI()


# app.include_router(users.router ,prefix = '/hi')  # whene used prefix = '/users' all routes start from /users
app.include_router(posts.router , prefix = '/posts')


@app.post("/users/{times}")
def say_hello(times : int):
    res = "Hello "*times
    return {"message":res}


#python-jose , passlib
 