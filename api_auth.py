from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import (CreateUser, Token, User,)
from service_auth import (AuthService, get_current_user,)

router = APIRouter( prefix='/auth')

@router.post('/sign-up', response_model=Token)
def sign_up(
    user_data: CreateUser,
    service: AuthService = Depends()
):
    return service.register_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    return service.authentificate_user(
        auth_data.username, 
        auth_data.password,
    )

@router.get('/user', response_model = User)
def get_user(user: User = Depends(get_current_user)):
    return user