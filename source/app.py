from flask import Flask
from flask_restful import Api

from source.employees.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
