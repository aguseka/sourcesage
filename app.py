from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from dotenv import load_dotenv
from db import db
import os


from resources.products import blp as ProductBlueprint
from resources.variants import blp as VariantsBlueprint

from resources.images import blp as ImageBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["API_TITLE"] = "SourceSage API Test"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ProductBlueprint)
    api.register_blueprint(VariantsBlueprint)
    api.register_blueprint(ImageBlueprint)

    return app
