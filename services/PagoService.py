from models.PagoModel import db, Pago

class PagoService:
    @staticmethod
    def create_pago(id_p, monto, fecha, estado):
        # Crea el objeto
        pago = Pago(id_p=id_p, monto=monto, fecha=fecha, estado=estado)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(pago)
        db.session.commit()
        return pago
    
    @staticmethod
    def get_all_pagos():
        return Pago.query.all()    