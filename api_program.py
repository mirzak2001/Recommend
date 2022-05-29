from fastapi import APIRouter
from fastapi import Depends
from models import User, product
from typing import List
from database import new_session
from sqlalchemy.orm import Session
from service_auth import get_current_user
import tables
import service_programs
from models import User

router = APIRouter( prefix='/run_program')

@router.post ('/1')
def recommendations_kMeans(user : User = Depends(get_current_user)):
    service_programs.new_experiment(user)
    return ("Program 1 has run successfully!")
