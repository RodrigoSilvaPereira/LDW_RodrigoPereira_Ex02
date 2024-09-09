from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Suplementos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.String(150))
    categoria = db.Column(db.String(150))
    descricao = db.Column(db.String(500))

    def __init__(self, titulo, ano, categoria, descricao):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.descricao = descricao
