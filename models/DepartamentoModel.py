from app import db
from sqlalchemy.orm import relationship
    
class Departamento(db.Model):
    id_dep = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    piso = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(35), nullable=False)

    residente_id = db.Column(db.Integer, db.ForeignKey('resident.rut'), nullable=True)  # Referencia al residente
    residente = relationship('Resident', back_populates='departamentos')  # Relación inversa desde Resident

    def serialize(self):
        return {
            'id': self.id_dep,
            'numero': self.numero,
            'piso': self.piso,
            'tipo': self.tipo,
            'residente': self.residente.serialize() if self.residente else None,
        }   