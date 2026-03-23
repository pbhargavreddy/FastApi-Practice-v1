from sqlalchemy import Column, Integer, String,DateTime
from backend.app.Database.database import Base
from datetime import datetime
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    last_updated = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow,nullable=False)