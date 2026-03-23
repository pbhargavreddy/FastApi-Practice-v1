from pydantic import BaseModel
from datetime import datetime

#base
class PostBase(BaseModel):
    title :str 
    content : str
# For post creating (request body)
class PostCreate(PostBase):
    pass

#For response
class PostResponse(PostBase):
    id : int
    created_at : datetime
    last_updated :datetime | None = None

    class Config:
        from_attributes = True
