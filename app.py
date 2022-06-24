from flask import Flask
from flask_restful import Api

import db
from config import Config
from models.user import User
from resources.user import UserListResource
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    app.config['FLASK_ADMIN_SWATCH'] = 'cyborg'
    admin = Admin(app, name='Anystore Requests', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))

    return app


def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, '/users/')


if __name__ == '__main__':
    app = create_app()

    app.run()
