from app import db
    
class Edificio(db.Model):
    id_e = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(35), nullable=False)
    ubicacion = db.Column(db.String(80), nullable=False)
    cantPisos = db.Column(db.Integer, nullable=False)
    cantDeptos = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id_e': self.id_e,
            'nombre': self.nombre,
            'ubicacion': self.ubicacion,
            'cantPisos': self.cantPisos,
            'cantDeptos': self.cantDeptos,
        }   