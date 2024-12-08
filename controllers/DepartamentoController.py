from services.DepartamentoService import DepartamentoService

class DepartamentoController:
    @staticmethod
    def create_departamento_controller(id_dep, numero, piso, tipo, residente_id, residente):
        return DepartamentoService.create_resident(id_dep, numero, piso, tipo, residente_id, residente)
    
    @staticmethod
    def get_departamento_controller():
        return DepartamentoService.get_all_residents()