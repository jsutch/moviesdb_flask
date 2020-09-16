from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_mail import Mail 

# Errors
from resources.errors import errors
# local creds
import creds

app = Flask(__name__)

# import JWT key
app.config["JWT_SECRET_KEY"] = creds.JWT_SECRET_KEY

#mail settings
app.config["MAIL_SERVER"] = creds.MAIL_SERVER
app.config["MAIL_PORT"] = creds.MAIL_PORT
app.config["MAIL_USERNAME"] = creds.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = creds.MAIL_PASSWORD

# avoiding a circular import with main/app
mail = Mail(app)
from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config["MONGODB_SETTINGS"] = {
    "db":'movie-bag',
    "username":creds.mongouser,
    "password":creds.mongopassword,
    "host":"mongodb://storage/movie-bag?authSource=admin",
}
app.config['PROPAGATE_EXCEPTIONS'] = False # custom exceptions fail without this

initialize_db(app)
initialize_routes(api)

# moved to run.py
# app.run(debug=True)
# app.run()