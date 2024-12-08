from models.EdificioModel import db, Edificio

class EdificioService:
    @staticmethod
    def create_edificio(id_e, nombre, ubicacion, cantPisos, cantDeptos):
        # Crea el objeto
        edificio = Edificio(id_e=id_e, nombre=nombre, ubicacion=ubicacion, cantPisos=cantPisos, cantDeptos=cantDeptos)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(edificio)
        db.session.commit()
        return edificio
    
    @staticmethod
    def get_all_edificios():
        return Edificio.query.all()    