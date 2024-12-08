from models.PersonalModel import db, Personal

class PersonalService:
    @staticmethod
    def create_personal(rut, nombre, cargo, horario):
        # Crea el objeto
        personal = Personal(rut=rut, nombre=nombre, cargo=cargo, horario=horario)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(personal)
        db.session.commit()
        return personal
    
    @staticmethod
    def get_all_personal():
        return Personal.query.all()    