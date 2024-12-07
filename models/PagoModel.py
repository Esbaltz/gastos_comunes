from app import db
    
class Pago(db.Model):
    id_p = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            'id_p': self.id_p,
            'monto': self.monto,
            'fecha': self.fecha,
            'estado': self.estado,
        }   