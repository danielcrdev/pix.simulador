from flask import Flask
import routes

nome_app = "pix_simulador"
versao_app = "v0_0_1"

app = Flask(nome_app + "_" + versao_app)


def create_app():
    app.register_blueprint(routes.get_blueprint())
    return app


if __name__ == '__main__':

    a = create_app()
    a.run()
