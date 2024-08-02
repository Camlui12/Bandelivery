from app import db

class Usuarios(db.Model):
    matricula = db.Column(db.String(11), primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    senha = db.Column(db.String(50), nullable = False)
    tipo = db.Column(db.String(5), nullable = False)
    endereco = db.Column(db.String(150), nullable = False)
    adm = db.Column(db.Boolean, nullable = False)

class Cardapios(db.Model):
    op_onivora = db.Column(db.String(50))
    op_veg = db.Column(db.String(50))
    guarnicao = db.Column(db.String(50))
    salada1 = db.Column(db.String(50))
    salada2 = db.Column(db.String(50))
    refresco = db.Column(db.String(50))
    dia = db.Column(db.String(7), primary_key =True)