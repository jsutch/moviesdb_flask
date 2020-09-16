from flask import Flask, request
from flask_restful import Resource, reqparse

class Test(Resource):
    """
    test harness. return whatever name passed
    """
    def get(self):
        """
        testing 
        """
        return "This is a web return", 200
