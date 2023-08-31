from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    fav1 = db.relationship("Fav", backref="user")

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    residents = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    surface_water = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    fav2 = db.relationship("Fav", backref="planets")

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=True, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    homeworld = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    vehicles = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    fav3 = db.relationship("Fav", backref="characters")

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "species": self.species,
            "vehicles": self.vehicles,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    consumables = db.Column(db.String(120), unique=True, nullable=False)
    crew = db.Column(db.String(120), unique=True, nullable=False)
    length = db.Column(db.String(80), unique=False, nullable=False)
    manufacturer = db.Column(db.String(80), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(80), unique=False, nullable=False)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    pilots = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    fav4 = db.relationship("Fav", backref="vehicles")
    

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "crew": self.crew,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "passengers": self.passengers,
            "pilots": self.pilots,
            "url": self.url,
            # do not serialize the password, its a security breach
        }
    
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    MGLT = db.Column(db.String(120), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    consumables = db.Column(db.String(120), unique=True, nullable=False)
    hyperdrive_rating = db.Column(db.String(80), unique=False, nullable=False)
    length = db.Column(db.String(80), unique=False, nullable=False)
    manufacturer = db.Column(db.String(80), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(80), unique=False, nullable=False)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    pilots = db.Column(db.String(80), unique=False, nullable=False)
    starship_class = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    fav5 = db.relationship("Fav", backref="starships")
    

    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "passengers": self.passengers,
            "pilots": self.pilots,
            "starship_class": self.starship_class,
            "url": self.url,
            # do not serialize the password, its a security breach
        }
    
class Fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    # user = db.relationship(User)
    # planets = db.relationship(Planets)
    # characters = db.relationship(Characters)
    # vehicles = db.relationship(Vehicles)
    # starships = db.relationship(Starships)
    

    def __repr__(self):
        return '<Fav %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
            "vehicles_id": self.vehicles_id,
            "starships_id": self.starships_id
            # do not serialize the password, its a security breach
        }