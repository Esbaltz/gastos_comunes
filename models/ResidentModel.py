from app import db
from enum import Enum
from sqlalchemy.orm import relationship

class TipoResidencia(Enum):
    arrendatario = "arrendatario"
    dueño = "dueño"
    
class Resident(db.Model):
    rut = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(35), nullable=False)
    tipo_residencia = db.Column(db.Enum(TipoResidencia), nullable=False)

    departamentos = db.relationship('Departamento', backref='resident', lazy=True)  # Relación uno a muchos

    def serialize(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'tipo_residencia': self.tipo_residencia.name,
            'departamentos': [departamento.serialize() for departamento in self.departamentos],
        }   