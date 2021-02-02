from flask import Flask, render_template
from flask_bootstrap import Bootstrap


from config import config


boot = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    boot.init_app(app)

    #blueprints
    from app.portfolio import portfolio
    app.register_blueprint(portfolio, url_prefix='/portfolio/')
    print(app.url_map)
    return app
