from app import create_app
from views.ResidentView import resident_blueprint
from views.DepartamentoView import departamento_blueprint

app = create_app()
app.register_blueprint(resident_blueprint)
app.register_blueprint(departamento_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
