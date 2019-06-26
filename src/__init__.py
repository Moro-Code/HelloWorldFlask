from flask import Flask
from src.views.helloworldview import bp
import os
# Flask application factory to set up and configure the application
def create_app(templates_path= './src/templates'):
    app = Flask(__name__)
    # register the blueprint 
    app.register_blueprint(bp)
    # specify that the blueprint should be on the main route
    app.add_url_rule("/", endpoint = "helloworld")
    # register the templates path
    app.template_folder = os.path.abspath(templates_path)

    return app
    

