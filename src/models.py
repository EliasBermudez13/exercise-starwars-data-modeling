import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstName = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Favorites(Base):
    user = relationship(User)
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_Id = Column(Integer, ForeignKey('user.id'))
    planets_Id = Column(Integer)
    vehicles_Id = Column(Integer)
    characters_Id = Column(Integer)

class Characters(Base):
    favorites = relationship(Favorites)
    __tablename__ = 'characters'
    id = Column(Integer, ForeignKey('favorites.characters_Id'), primary_key=True)
    name = Column(String(250)) 
    url = Column(String(250), nullable=False)
    details_Id = Column(Integer)

class Vehicles(Base):
    favorites = relationship(Favorites)
    __tablename__ = 'vehicles'
    id = Column(Integer, ForeignKey('favorites.vehicles_Id'), primary_key=True)
    name = Column(String(250)) 
    url = Column(String(250), nullable=False)
    details_Id = Column(Integer)

class Planets(Base):
    favorites = relationship(Favorites)
    __tablename__ = 'planets'
    id = Column(Integer, ForeignKey('favorites.planets_Id'), primary_key=True)
    name = Column(String(250)) 
    url = Column(String(250), nullable=False)
    details_Id = Column(Integer)

class CharactersDetails(Base):
    characters = relationship(Characters)
    vehicles = relationship(Vehicles)
    planets = relationship(Planets)
    __tablename__ = 'charactersDetails'
    id = Column(Integer, ForeignKey('characters.details_Id'), primary_key=True)
    height = Column(String(250))
    mass = Column(String(250))
    hairColor = Column(String(250))
    skinColor = Column(String(250))
    eyeColor = Column(String(250))
    birthYear = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250), ForeignKey('planets.url'))  
    films = Column(String(250))
    species = Column(String(250))
    vehicles = Column(String(250), ForeignKey('vehicles.url'))  
    starships = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class VehiclesDetails(Base):
    characters = relationship(Characters)
    vehicles = relationship(Vehicles)
    __tablename__ = 'vehiclesDetails'
    id = Column(Integer, ForeignKey('vehicles.details_Id'), primary_key=True)
    cargoCapacity = Column(String(250))
    consumables = Column(String(250))
    costInCredits = Column(String(250))
    created = Column(String(250))
    crew = Column(String(250))
    edited = Column(String(250))
    length = Column(String(250))
    manufactured = Column(String(250))
    maxAtmSpeed = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))
    pilots = Column(String(250), ForeignKey('characters.url'))
    films = Column(String(250))
    vehicleClass = Column(String(250))

class PlanetsDetails(Base):
    characters = relationship(Characters)
    planets = relationship(Planets)
    __tablename__ = 'planetsDetails'
    id = Column(Integer, ForeignKey('planets.details_Id'), primary_key=True)
    climate = Column(String(250))
    created = Column(String(250))
    diameter = Column(String(250))
    edited = Column(String(250))
    films = Column(String(250))
    gravity = Column(String(250))
    orbitalPeriod = Column(String(250))
    population = Column(String(250))
    residents = Column(String(250), ForeignKey('characters.url'))
    rotationPeriod = Column(String(250))
    surfaceWater = Column(String(250))
    terrain = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
