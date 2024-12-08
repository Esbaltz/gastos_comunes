from models.ResidentModel import db, Resident

class ResidentService:
    @staticmethod
    def create_resident(rut, nombre, tipo_residencia, departamentos):
        # Crea el objeto
        resident = Resident(rut=rut, nombre=nombre, tipo_residencia=tipo_residencia, departamentos=departamentos)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(resident)
        db.session.commit()
        return resident
    
    @staticmethod
    def get_all_residents():
        return Resident.query.all()    