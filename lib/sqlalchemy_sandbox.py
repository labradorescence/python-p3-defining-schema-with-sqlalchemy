#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #Base is a parent object. this sandbox is inheriting from the declarative_base object.

class Student(Base):
    __tablename__ = ' students ' #this attribute -> SQL table name

    id =  Column(Integer(), primary_key=True) #column and primary key
    name = Column(String()) #column
    pass

if __name__ == '__main__': #to persist
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    pass