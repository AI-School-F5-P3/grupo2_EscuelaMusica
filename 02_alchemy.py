#Primero hay que hacer la importación de las librerías de ALCHEMY
#pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
