from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    apellido = db.Column(db.String(120), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido
            # do not serialize the password, its a security breach
        }

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    apellido = db.Column(db.String(120), unique=False, nullable=False)
    documento = db.Column(db.Integer, unique=True, nullable=False)
    direccion = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
        
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "documento": self.documento,
            "direccion": self.direccion,
            "email": self.email
            }

class Producto(db.Model):
    __tablename__ = "producto"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    descripcion = db.Column(db.String(120), unique=False, nullable=False)
    talla = db.Column(db.String(80), unique=False, nullable=False)
    precio = db.Column(db.Integer, unique=False, nullable=False)
    imagen = db.Column(db.String(1200), unique=False, nullable=False)
    cantidad = db.Column(db.String(80), unique=False, nullable=False)     
        
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "talla": self.talla,
            "precio": self.precio,
            "imagen": self.imagen,
            "cantidad": self.cantidad
        }         

    def get_content(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "talla": self.talla,
            "precio": self.precio,
            "imagen": self.imagen,
            "cantidad": self.cantidad
        }

class Proveedor(db.Model):
    __tablename__ = "proveedor"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    telefono = db.Column(db.String(90), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    saldo = db.Column(db.Integer, unique=False, nullable=False)
        
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "saldo": self.saldo
        }    