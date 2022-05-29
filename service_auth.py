from datetime import datetime, timedelta
from http.client import HTTPException
from logging import exception
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt
from pydantic import ValidationError
from jose import (JWTError, jwt, )
from database import Session, new_session

import tables
from models import (CreateUser, User as ModelUser, Token,)
from database import new_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = '/auth/sign-in/')


class AuthService:
    @classmethod
    def verify_password(cls, plain_pass: str, phash: str) -> bool:
        bcrypt.verify(plain_pass, phash)

    @classmethod
    def phash(cls, password:str)-> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token (cls, token: str) -> ModelUser:
       
        try:
            payload = jwt.decode(token,
             'GngdNE8gneg9etmewpqp3ibnde7dneJf',
              algorithms = 'HS256')
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = ModelUser.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user 

    @classmethod
    def create_token (cls, user: tables.User) -> Token:
        user_data = ModelUser.from_orm(user)

        now = datetime.utcnow()
        payload = {
            'iat':now,
            'nbf':now,
            'exp':now+ timedelta(seconds = 3600),
            'sub':str(user_data.id),
            'user':user_data.dict(),
        }
        token = jwt.encode(
            payload,
            'GngdNE8gneg9etmewpqp3ibnde7dneJf',
            algorithm = 'HS256'   
        )

        return Token(access_token=token)

    def __init__ (self, session: Session = Depends(new_session)):
        self.session = session
    def register_user (self, user_data: CreateUser) -> Token:
        
        user = tables.User(
            email = user_data.email,
            username = user_data.username,
            passwordhash = self.phash(user_data.password)

        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authentificate_user(self, username: str, password: str) -> Token:

        exception = HTTPException("Incorrect username/password")

        user = (
            self.session.
            query(tables.User).filter(tables.User.username == username).first())

        if not user:
            raise exception
        
        if self.verify_password ('string', user.passwordhash):
            raise exception

        return self.create_token (user)



def get_current_user (token: str = Depends(oauth2_scheme)) -> ModelUser:
    return AuthService.validate_token(token)