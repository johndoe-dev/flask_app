from flask import Flask
from flask_restplus import Resource, Api


# Create a Flask WSGI application
app = Flask(__name__)
# Create a Flask-RESTPlus API
api = Api(app)


# Create a URL route to this resource
@api.route('/hello')
# Create a RESTful resource
class HelloWorld(Resource):
    # Create GET endpoint
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

