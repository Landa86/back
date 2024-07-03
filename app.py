from flask import Flask,render_template
from config import Config
from extensions import db
from flask_migrate import Migrate
from routes import main



def create_app():
    app = Flask (__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:45851290@127.0.0.1:3306/back"
    app.config.from_object(Config)
    extensions(app) 
    register_resources(app)
    return app

def extensions(app):
        db.init_app(app)
        migrate = Migrate(app,db)


def register_resources(app):
    app.register_blueprint(main)
    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
