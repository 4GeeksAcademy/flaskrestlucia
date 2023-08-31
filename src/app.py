"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Vehicles, Starships, Fav

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)




##endpoints


#consultar todos los usuarios
@app.route('/user', methods=['GET'])
def handle_hello():
#le hago consulta de todos los usuarios de la tabla
    all_users=User.query.all()
     
#mapeamos el array y [<User>] convetimos en un objeto con serialize
    results = list(map(lambda item: item.serialize(), all_users))
    # print(results)#print para ver lo que guardo
    if results == []:#si el resultado es un objeto vacio no hay usuario
        return jsonify({"msg":"no hay usuario"}), 404 

    #devuelve respuesta con resultados de la consulta
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }

    return jsonify(response_body), 200


#consultar un usuario
@app.route("/user/<int:user_id>", methods=['GET'])
def get_one_user(user_id):#se ejecuta una funcion

    user_query=User.query.filter_by(id=user_id).first()#se una el filter_by para filtrar por user_id en este caso
    #lo busca en la lista
     
    if user_query is None:#si no hay valor el usuario no existe
        return jsonify({"msg":"no extiste el usuario"}), 404 

    # si existe devuelve respuesta con resultados de la consulta
    response_body = {
        "msg": "este es el usuario",
        "results": user_query.serialize()#con serialize lo convierto
    }

    return jsonify(response_body), 200




#llamo a la app y le digo que le quiero crear una ruta con el metodo que quiera
@app.route('/planets', methods=['GET'])
def get_planets():#se ejecuta una funcion

    all_planets=Planets.query.all()
     
#mapeamos el array y [<User>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), all_planets))
    # print(results)#print para ver lo que guardo
    if results == []:
        return jsonify({"msg":"no hay planetas"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "estos son los planetas",
        "results": results
    }

    return jsonify(response_body), 200


@app.route("/planets/<int:planet_id>", methods=['GET'])
def get_one_planets(planet_id):#se ejecuta una funcion

    planet_query=Planets.query.filter_by(id=planet_id).first()
     
#mapeamos el array y [<User>] convetimos en un objeto
    # results = list(map(lambda item: item.serialize(), all_planets))
    # print(results)#print para ver lo que guardo
    if planet_query is None:
        return jsonify({"msg":"no extiste el planeta"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "este es el planeta",
        "results": planet_query.serialize()
    }

    return jsonify(response_body), 200



@app.route('/characters', methods=['GET'])
def get_characters():#se ejecuta una funcion

    all_characters=Characters.query.all()
     
#mapeamos el array y [<User>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), all_characters))
    # print(results)#print para ver lo que guardo
    if results == []:
        return jsonify({"msg":"no hay personajes"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "estos son los personajes",
        "results": results
    }

    return jsonify(response_body), 200


@app.route("/characters/<int:character_id>", methods=['GET'])
def get_one_character(character_id):#se ejecuta una funcion

    character_query=Characters.query.filter_by(id=character_id).first()
     
#mapeamos el array y [<User>] convetimos en un objeto
    # results = list(map(lambda item: item.serialize(), all_planets))
    # print(results)#print para ver lo que guardo
    if character_query is None:
        return jsonify({"msg":"no extiste el personaje"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "este es el personaje",
        "results": character_query.serialize()
    }

    return jsonify(response_body), 200


@app.route('/vehicles', methods=['GET'])
def get_vehicles():#se ejecuta una funcion

    all_vehicles=Vehicles.query.all()
     
#mapeamos el array y [<User>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), all_vehicles))
    # print(results)#print para ver lo que guardo
    if results == []:
        return jsonify({"msg":"no hay vehiculos"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "estos son los vehiculos",
        "results": results
    }

    return jsonify(response_body), 200



@app.route("/vehicles/<int:vehicle_id>", methods=['GET'])
def get_one_vehicle(vehicle_id):#se ejecuta una funcion

    vehicle_query=Vehicles.query.filter_by(id=vehicle_id).first()
     
#mapeamos el array y [<User>] convetimos en un objeto
    # results = list(map(lambda item: item.serialize(), all_planets))
    # print(results)#print para ver lo que guardo
    if vehicle_query is None:
        return jsonify({"msg":"no extiste el vehiculo"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "este es el vehiculo",
        "results": vehicle_query.serialize()
    }

    return jsonify(response_body), 200


@app.route('/starships', methods=['GET'])
def get_starships():#se ejecuta una funcion

    all_starships=Starships.query.all()
     
#mapeamos el array y [<User>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), all_starships))
    # print(results)#print para ver lo que guardo
    if results == []:
        return jsonify({"msg":"no hay naves"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "estos son las naves",
        "results": results
    }

    return jsonify(response_body), 200




@app.route("/starships/<int:starship_id>", methods=['GET'])
def get_one_starship(starship_id):#se ejecuta una funcion

    starship_query=Starships.query.filter_by(id=starship_id).first()
     
#mapeamos el array y [<User>] convetimos en un objeto
    # results = list(map(lambda item: item.serialize(), all_planets))
    # print(results)#print para ver lo que guardo
    if starship_query is None:
        return jsonify({"msg":"no extiste esta nave"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "esta es la nave",
        "results": starship_query.serialize()
    }

    return jsonify(response_body), 200

#trae un favorito
@app.route('/user/fav', methods=['GET'])
def get_fav():#se ejecuta una funcion

    all_fav=Fav.query.all()

#mapeamos el array y [<User>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), all_fav))
    print(results)#print para ver lo que guardo
    if (results == []):
        return jsonify({"msg":"no hay favoritos"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "estos son los favoritos",
        "results": results
    }

    return jsonify(response_body), 200

@app.route('/user/fav', methods=['GET'])
def get_one_fav(id):#se ejecuta una funcion

    one_fav=Fav.query.filter_by(user_id = id)

#mapeamos el array y [<>] convetimos en un objeto
    results = list(map(lambda item: item.serialize(), one_fav))
    print(results)#print para ver lo que guardo
    if (results == []):#si el resultado es un objeto vacio entones no hay usuario
        return jsonify({"msg":"no encontrado"}), 404 

    #devuelve respuesta con resuñtados de la consulta
    response_body = {
        "msg": "favorito",#?????
        "results": results
    }

    return jsonify(response_body), 200

#agrega planeta un favorito

#la ruta para llevar planetas a favoritos <que es int:plantes?>
@app.route("/fav/planets/<int:planeta_id>", methods=['POST'])
def create_favorito_planet(planeta_id):#se ejecuta una funcion con el parametro que es el id de planeta
   
    request_body= request.get_json(force=True) #obtiene el body que mando desde posman
    print(request_body)#(porpiedad de la tabla = request body que es lo que agregue en el body)
   
    user_query=User.query.filter_by(id = request_body["user_id"]).first()#filtra por el id especificado para ver si el id ya existe
    if user_query is None:#si el id no aparece el usuario no esta rigistrado
        return jsonify({"msg":"no esta registrado"}), 404 
    
    #preguntar para que es esa parte
   
              #class de la tabla    #id prop tabla  # planets_id lo que viene por url en posman
    planet_query=Planets.query.filter_by(id = planeta_id).first()#filtr por el id del planeta 
    if planet_query is None:
        return jsonify({"msg": "el planeta no existe"}), 404

                            #user_id de la tabla #request body lo que viene del body de posman
    fav = Fav.query.filter_by(user_id=request_body["user_id"]).filter_by(planets_id = planeta_id).first() #filtra, no deja pasar los que no coinciden, trae los que coinciden los velores de user_id de la tabla favoritos con lo que pongo en el body
    # busca un usuario con esa id si hay, chequear si tiene ese id del planeta
        #el fav recorre todos los favoritos del user_id
    if fav:  
        return jsonify({"msg":"ya esta agregado este planeta"}), 404 #retorna q ya se habia agregado


    new_planet_fav=Fav(user_id=request_body["user_id"],planets_id=planeta_id)
    db.session.add(new_planet_fav)
    db.session.commit()
            
    
  
    request_body = {#si no entra en el if agraga el favorito
    "msg": "favorito agregado",
    }    
    return jsonify(request_body), 200



#agragar character como favorito
@app.route("/fav/characters/<int:personajes_id>", methods=['POST'])
def create_favorito_character(personajes_id):#se ejecuta una funcion con el parametro que es el id de planeta
   
    request_body= request.get_json(force=True) #obtiene el body que mando desde posman
    print(request_body)#(porpiedad de la tabla = request body que es lo que agregue en el body)
   
    user_query=User.query.filter_by(id = request_body["user_id"]).first()#filtra por el id especificado para ver si el id ya existe
    if user_query is None:#si el id no aparece el usuario no esta rigistrado
        return jsonify({"msg":"no esta registrado"}), 404 
    
    #preguntar para que es esa parte
   
              #class de la tabla    #id prop tabla  # planets_id lo que viene por url en posman
    character_query=Characters.query.filter_by(id = personajes_id).first()#filtr por el id del planeta 
    if character_query is None:
        return jsonify({"msg": "el personaje no existe"}), 404

                            #user_id de la tabla #request body lo que viene del body de posman
    fav = Fav.query.filter_by(user_id=request_body["user_id"]).filter_by(characters_id = personajes_id).first() #filtra, no deja pasar los que no coinciden, trae los que coinciden los velores de user_id de la tabla favoritos con lo que pongo en el body
    # busca un usuario con esa id si hay, chequear si tiene ese id del planeta
        #el fav recorre todos los favoritos del user_id
    if fav:  
        return jsonify({"msg":"ya esta agregado este personaje"}), 404 #retorna q ya se habia agregado


    new_character_fav=Fav(user_id=request_body["user_id"],characters_id = personajes_id)
    db.session.add(new_character_fav)
    db.session.commit()
            
    
  
    request_body = {#si no entra en el if agraga el favorito
    "msg": "favorito agregado",
    }    
    return jsonify(request_body), 200



#borrar character como favorito
@app.route("/fav/characters/<int:personajes_id>", methods=['DELETE'])
def borrar_favorito_character(personajes_id):#se ejecuta una funcion con el parametro que es el id de planeta
   
    request_body= request.get_json(force=True) #obtiene el body que mando desde posman
    print(request_body)#(porpiedad de la tabla = request body que es lo que agregue en el body)
   
    user_query=User.query.filter_by(id = request_body["user_id"]).first()#filtra por el id especificado para ver si el id ya existe
    if user_query is None:#si el id no aparece el usuario no esta rigistrado
        return jsonify({"msg":"no esta registrado"}), 404 
    
    #preguntar para que es esa parte
   
              #class de la tabla    #id prop tabla  # planets_id lo que viene por url en posman
    character_query=Characters.query.filter_by(id = personajes_id).first()#filtr por el id del planeta 
    if character_query is None:
        return jsonify({"msg": "el personaje no existe"}), 404

                            #user_id de la tabla #request body lo que viene del body de posman
    fav = Fav.query.filter_by(user_id=request_body["user_id"]).filter_by(characters_id = personajes_id).first() #filtra, no deja pasar los que no coinciden, trae los que coinciden los velores de user_id de la tabla favoritos con lo que pongo en el body
    # # busca un usuario con esa id si hay, chequear si tiene ese id del planeta
    #     #el fav recorre todos los favoritos del user_id
    # if fav:  
    #     return jsonify({"msg":"ya esta agregado este personaje"}), 404 #retorna q ya se habia agregado


    # new_character_fav=Fav(user_id=request_body["user_id"],characters_id = personajes_id)
    db.session.delete(fav)
    db.session.commit()
            
    
  
    request_body = {#si no entra en el if agraga el favorito
    "msg": "se borro",
    }    
    return jsonify(request_body), 200


#borrar planeta como favorito
@app.route("/fav/planets/<int:planeta_id>", methods=['DELETE'])
def borrar_favorito_planet(planeta_id):#se ejecuta una funcion con el parametro que es el id de planeta
   
    request_body= request.get_json(force=True) #obtiene el body que mando desde posman
    print(request_body)#(porpiedad de la tabla = request body que es lo que agregue en el body)
   
    user_query=User.query.filter_by(id = request_body["user_id"]).first()#filtra por el id especificado para ver si el id ya existe
    if user_query is None:#si el id no aparece el usuario no esta rigistrado
        return jsonify({"msg":"no esta registrado"}), 404 
    
    #preguntar para que es esa parte
   
              #class de la tabla    #id prop tabla  # planets_id lo que viene por url en posman
    planet_query=Planets.query.filter_by(id = planeta_id).first()#filtr por el id del planeta 
    if planet_query is None:
        return jsonify({"msg": "el pplaneta no existe"}), 404

                            #user_id de la tabla #request body lo que viene del body de posman
    fav = Fav.query.filter_by(user_id=request_body["user_id"]).filter_by(planets_id = planeta_id).first() #filtra, no deja pasar los que no coinciden, trae los que coinciden los velores de user_id de la tabla favoritos con lo que pongo en el body
    # # busca un usuario con esa id si hay, chequear si tiene ese id del planeta
    #     #el fav recorre todos los favoritos del user_id
    # if fav:  
    #     return jsonify({"msg":"ya esta agregado este personaje"}), 404 #retorna q ya se habia agregado


    # new_character_fav=Fav(user_id=request_body["user_id"],characters_id = personajes_id)
    db.session.delete(fav)
    db.session.commit()
            
    
  
    request_body = {#si no entra en el if agraga el favorito
    "msg": "se borro",
    }    
    return jsonify(request_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
