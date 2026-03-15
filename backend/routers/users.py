from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
def root():
    return {"Message":"My Backend is alive"}



class User(BaseModel):
    name: str
    age : int
    email : str | None = None # Here None = None means email is not required attribute. it is not mandatory
    bank_balance : int = 0 # here =0 after datatype means that if user didnt give this attribute take 0 as default

@router.post("/")
def create_user(user : User):
    return{
        "Message":"User successfully created",
        "user":user
    }
@router.get("/")
def get_users():
    return {'Name':"Bhargav"}

