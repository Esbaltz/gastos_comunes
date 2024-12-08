from app import create_app
from views.ResidentView import resident_blueprint
from views.DepartamentoView import departamento_blueprint
from views.PagoViews import pago_blueprint
from views.SolicitudViews import solicitud_blueprint
from views.EdificioViews import edificio_blueprint
from views.PersonalViews import personal_blueprint

app = create_app()
app.register_blueprint(resident_blueprint)
app.register_blueprint(departamento_blueprint)
app.register_blueprint(pago_blueprint)
app.register_blueprint(solicitud_blueprint)
app.register_blueprint(edificio_blueprint)
app.register_blueprint(personal_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
