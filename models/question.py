
from sqlmodel import SQLModel,Field
from typing import Optional,List


class Question(SQLModel,table=True):
    id:Optional[int] = Field(primary_key=True,default=None)
    question:str = Field(default=None)
    answer:str = Field(default=None)
    options:str = Field(default=None)

