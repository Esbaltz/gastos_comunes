from app import db
    
class Personal(db.Model):
    rut = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(35), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            'rut': self.rut,
            'nombre': self.nombre,
            'cargo': self.cargo,
            'horario': self.horario,
        }   