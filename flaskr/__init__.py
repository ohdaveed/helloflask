"""Module that creates the Flask application and registers the blueprints."""
import os
from dotenv import load_dotenv
from flask import Flask
from . import db
from . import auth
from . import blog

load_dotenv()  # Load environment variables from .env file


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.getenv("SECRET_KEY"),
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    app.add_url_rule("/", endpoint="index")

    return app
