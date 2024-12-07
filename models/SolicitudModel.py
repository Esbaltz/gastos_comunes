from app import db
    
class Solicitud(db.Model):
    id_s = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    descripion = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id_s': self.id_s,
            'tipo': self.tipo,
            'fecha': self.fecha,
            'estado': self.estado,
            'descripcion': self.descripion,
        }   