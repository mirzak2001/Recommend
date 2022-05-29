from ast import For
from enum import unique
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    passwordhash = sa.Column(sa.String)

class Category(Base):
    __tablename__ = 'Categories'
    id = sa.Column(sa.Integer, primary_key=True)
    Title = sa.Column(sa.String, unique = True)


class Product(Base):
    __tablename__ = 'Products'
    id = sa.Column(sa.Integer, primary_key=True)
    Title = sa.Column(sa.String)
    Description = sa.Column(sa.String)
    Category = sa.Column(sa.String, ForeignKey('Categories.Title')) 

class Program(Base):
    __tablename__ = 'programs'
    id = sa.Column(sa.Integer, primary_key=True)
    Title = sa.Column(sa.String)
    Path = sa.Column(sa.String) 

class Experiment(Base):
    __tablename__ = 'experiments'
    id = sa.Column(sa.Integer, primary_key=True)
    program = sa.Column(sa.String)
    User = sa.Column(sa.String, ForeignKey('Users.username'))
    StartDateTime = sa.Column(sa.DateTime)
    EndDateTime = sa.Column(sa.DateTime)


class Recommendation(Base):
    __tablename__ = 'recommendations'
    id = sa.Column(sa.Integer, primary_key = True)
    experiment_id = sa.Column(sa.Integer)
    product_id = sa.Column(sa.Integer, ForeignKey ('Products.id'))
    cluster = sa.Column(sa.Integer)
    
                         
