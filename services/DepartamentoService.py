from models.DepartamentoModel import db, Departamento

class DepartamentoService:
    @staticmethod
    def create_departamento(id_dep, numero, piso, tipo):
        # Crea el objeto
        departamento = Departamento(id_dep=id_dep, numero=numero, piso=piso, tipo=tipo)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(departamento)
        db.session.commit()
        return departamento
    
    @staticmethod
    def get_all_residents():
        return Departamento.query.all()    