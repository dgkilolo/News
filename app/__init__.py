from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from .requests import configure_request



def create_app(config_name):

    app = Flask(__name__,instance_relative_config = True)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    Bootstrap(app)

    
    

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    
    configure_request(app)

    # Will add the views and forms

    return app

