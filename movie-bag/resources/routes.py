from .movie import MoviesApi, MovieApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword
from .test import Test

def initialize_routes(api):
    apy.add_resource(Test,'/')
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
    