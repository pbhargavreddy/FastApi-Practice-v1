from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
class User(BaseModel):
    name : str
    age : int

@router.get("/hello/{name}")
def pathParameter(name:str):
    return {f"Helllo {name}"}

@router.get("/users/")    # /users/?Limit=2&&page='a'
def queryParameter(Limit : int, page: str):
    return {f"{Limit}, {page}"}

@router.get("/user")
def requestBody(user : User):
    return user 
# update,delete