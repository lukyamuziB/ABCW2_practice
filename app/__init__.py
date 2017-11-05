from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(config['development'])
    config['development'].init_app(app)

    bootstrap.init_app(app)

    #Registering blueprint
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)


    return app
