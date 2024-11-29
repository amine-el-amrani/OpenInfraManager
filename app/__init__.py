from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from .routes import server_bp, images_bp
    app.register_blueprint(server_bp, url_prefix="/api")
    app.register_blueprint(images_bp, url_prefix="/api")

    return app