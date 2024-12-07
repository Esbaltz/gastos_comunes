from app import db
    
class Departamento(db.Model):
    id_dep = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    piso = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(35), nullable=False)

    def serialize(self):
        return {
            'id': self.id_dep,
            'numero': self.numero,
            'piso': self.piso,
            'tipo': self.tipo,
        }   