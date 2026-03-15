from fastapi import FastAPI
from routers import users,inputTypes
from pydantic import BaseModel   #BaseModel is used to check Data type and also type convertion.


app = FastAPI()
app.include_router(users.router , prefix = '/users')  # whene used prefix = 'users' all routes start from /users
app.include_router(inputTypes.router)



#python-jose , passlib
