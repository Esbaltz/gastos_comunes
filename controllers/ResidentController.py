from services.ResidentService import ResidentService

class ResidentController:
    @staticmethod
    def create_resident_controller(rut, nombre, tipo_residencia):
        return ResidentService.create_resident(rut, nombre, tipo_residencia)
    
    @staticmethod
    def get_resident_controller():
        return ResidentService.get_all_residents()