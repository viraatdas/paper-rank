from pydantic import BaseModel
from datetime import datetime
from typing import List

class PaperBase(BaseModel):
    title: str
    abstract: str
    url: str
    arxiv_id: str

class PaperCreate(PaperBase):
    pass

class Paper(PaperBase):
    id: int
    votes: int
    created_at: datetime
    comments: List["Comment"] = []

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    paper_id: int
    created_at: datetime

    class Config:
        orm_mode = True
