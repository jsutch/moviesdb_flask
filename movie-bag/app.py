from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
#
import creds

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = creds.JWT_SECRET_KEY

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config["MONGODB_SETTINGS"] = {
    "db":'movie-bag',
    "username":creds.mongouser,
    "password":creds.mongopassword,
    "host":"mongodb://storage/movie-bag?authSource=admin",
}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)