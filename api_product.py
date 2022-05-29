from fastapi import APIRouter
from fastapi import Depends
from models import product
from typing import List
from database import new_session
from sqlalchemy.orm import Session
from service_auth import get_current_user
import tables
from models import User




router = APIRouter( prefix='/products')

@router.get('/{product_id}' )
def get_product_bi_id (product_id : int, session: Session = Depends(new_session),
user : User = Depends(get_current_user)):
    return session.query(tables.Product).filter(tables.Product.id == product_id).first()

@router.get('/get_similar/{product_title}')
def get_similar_products (product_title : str, session: Session = Depends(new_session), 
):
    search = "%{}%".format(product_title)
    return session.query(tables.Product).filter(tables.Product.Title.like(search))
