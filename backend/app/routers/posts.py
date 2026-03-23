from fastapi import APIRouter,Response,status,HTTPException  #response used to change response statuscodes.status provides codes.HTTPEXECPTION used to raise errors and change status codes
from pydantic import BaseModel
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.Database.database import SessionLocal,engine,get_db
from backend.app.Database.models import Base,Post
from backend.app.schema import PostBase,PostCreate,PostResponse
from typing import List
router = APIRouter()

#_________post_________
# Create post

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_post(post : PostCreate , db : Session = Depends(get_db)):
    new_post = Post(title = post.title,content = post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"Message":"post created"}


#_________get_________
# get all posts
@router.get('/',response_model=List[PostResponse])
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(Post).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No posts uploaded yet')
    return posts

#get single post 
@router.get('/{id}',response_model = PostResponse)
def get_one_post(id : int, db : Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if  not post :
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    return post

#____delete______
#delete post
@router.delete('/{id}')
def delete_post(id:int , db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="No content")
    post.delete(synchronize_session = False)
    db.commit()
    return {"message":"deleted"}


#_________put_________
#Update post
@router.put('/{id}')
def update_post(id:int,post_body:PostCreate , db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id)
    if not post.first():
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no post with id: {id} ")
    post_dict = post_body.model_dump()
    post.update({
        "title":post_dict["title"],
        "content":post_dict["content"]
    })
    db.commit()
    return {"Message":"post updated"}

