import string
from pydantic import BaseModel
from sqlalchemy import NVARCHAR


class BaseUser(BaseModel):
    email:str
    username:str

class CreateUser(BaseUser):
    password: str


class User(BaseUser):
    id: int 
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class product(BaseModel):
    id : int
    Title : str
    Description : str
    Category : str
    class Config:
        orm_mode = True
