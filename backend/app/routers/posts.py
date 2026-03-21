from fastapi import APIRouter,Response,status  #response used to change response statuscodes.status provides codes
from fastapi import HTTPException  # used to rise errors
from pydantic import BaseModel
router = APIRouter()


class Post(BaseModel):
    # def __init__(self):
        title :str
        data : str
        # tags : str | None = None

def isIdExist(id:int):
     for data in database:
         if data['id'] == id :
              return True
     return False

def getIndex(id:int):
     if isIdExist(id):
        for i in range(len(database)):
            if  database[i]['id'] == id:
                return i
        return None
     

database = [{"title":"My first post","data":"img1uy3y2y81.jpeg","id":-1}]



@router.get('/')
def get_posts(response : Response):
    posts = database[1:]
    if not posts:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='No posts')
        # or
        #  response.status_code = status.HTTP_400_BAD_REQUEST
        #  return {"message":"No posts"}
    return posts

@router.post('/')
def create_post(post : Post):
    p = post.dict()
    prev_id = database[-1].get("id",0)
    p["id"] = prev_id + 1
    database.append(p)
    return {"Message":"post created"}

@router.delete('/{id}')
def delete_post(id:int):
    idx = getIndex(id)
    if not idx:
          raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"no content available with id: {id}")
    database.pop(idx)
    return {"deleted post":id}

@router.get('/{id}')
def get_one_post(id : int):
    idx = getIndex(id)
    if not idx :
          raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"Post with the id: {id} does not exit")
    return database[idx]

@router.put('/{id}')
def update_post(id:int,post:Post):
    idx = getIndex(id)
    if not idx:
          raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"no post with id: {id} ")
    post_dict = post.model_dump()
    post_dict['id'] = id
    database[idx] = post_dict
    return {"message":f"Updated succesfully"}
