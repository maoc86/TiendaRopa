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
from models import db, User, Producto
#from models import Person

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

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['GET'])
def handle_users(user_id=None):
    if user_id is None:
        users = User.query.all()
        return jsonify([x.serialize() for x in users]), 200

    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return jsonify(user.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400

  
@app.route('/producto', methods=['GET', 'POST'])
def handle_producto():

    if request.method == 'POST':
        body = request.get_json()
        producto = Producto(
            nombre=body['nombre'], 
            descripcion= body['descripcion'],
            talla=body['talla'],
            precio=body['precio']
            )
        
        db.session.add(producto)
        db.session.commit()
        response_body = {
        "msg": "Producto agregado correctamente!"
        }
        return jsonify(response_body), 200

    if request.method == 'GET':
        all_producto = Producto.query.all()
        all_producto =list(map(lambda x: x.serialize(), all_producto))
        response_body = all_producto
        return jsonify(response_body), 200

@app.route('/producto/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto_query = Producto.query.get(producto_id)
    
    if not producto_query:
        response_body = {
            "msg": "producto no existe."
        }
        return jsonify(response_body), 200

    data_producto = producto_query.serialize()
    return jsonify({
        "result": data_producto
    }), 200

@app.route('/producto/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = Producto.query.filter_by(id=producto_id).one_or_none()
    if producto == None:
        return 'No existe el Producto', 404
    else:
        try:
            db.session.delete(producto)
            db.session.commit()
            return "Se ha borrado el Producto sastifastoriamente", 200
        except Exception as err:
            return 'Ha ocurrido un error', 500

@app.route('/producto/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    body = request.json
    if "descripcion" not in body:
        return "Este producto no tiene descripcion", 400
    if "talla" not in body:
        return "Este producto no tiene talla", 400
    else:
        producto = Producto.query.filter_by(id=producto_id).one_or_none()
        if producto == None:
            return "No existe el producto", 400            
        try:
            producto.descripcion = body['descripcion']
            producto.tall = body['talla']
            db.session.commit() 
            return jsonify(producto.get_content()), 201
        except Exception as err:
            return jsonify({ "error": "Ha ocurrido un error de servidor"}), 500



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
