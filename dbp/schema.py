import enum

from sqlalchemy import MetaData, Column, Integer, Enum, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema='playground'))


class Species(enum.Enum):
    Puma = 1
    Tiger = 2
    Ocelot = 3
    Jaguar = 4
    Lion = 5
    Cheetah = 6


class Kitties(Base):
    __tablename__ = 'kitties'

    id = Column(Integer, primary_key=True)
    species = Column(Enum(Species), nullable=False)
    name = Column(String)


# class Woofs(Base):
#     """
#     a table with a trigger on it

#     :param Base: _description_
#     """
#     __tablename__ = 'woofs'
