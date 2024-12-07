from app import db
from enum import Enum

class TipoResidencia(Enum):
    arrendatario = "arrendatario"
    dueño = "dueño"
    
class Resident(db.Model):
    rut = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(35), nullable=False)
    tipo_residencia = db.Column(db.Enum(TipoResidencia), nullable=False)

    def serialize(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'tipo_residencia': self.tipo_residencia.name,
        }   