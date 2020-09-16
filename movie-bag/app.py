from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
import creds

app = Flask(__name__)
api = Api(app)


app.config["MONGODB_SETTINGS"] = {
    "db":'movie-bag',
    "username":creds.mongouser,
    "password":creds.mongopassword,
    "host":"mongodb://storage/movie-bag?authSource=admin",
}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)