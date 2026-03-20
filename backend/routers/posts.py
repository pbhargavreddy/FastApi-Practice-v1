from fastapi import APIRouter,Response,status  #response used to change response statuscodes.status provides codes
from fastapi import HTTPException  # used to rise errors
from pydantic import BaseModel
router = APIRouter()


class Post(BaseModel):
    # def __init__(self):
        title :str
        data : str
        # tags : str | None = None
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