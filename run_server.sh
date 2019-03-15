#!/bin/sh

# The FLASK_APP environment variable is used to specify how to load the application.
export FLASK_APP=flask_app.py

# Setting FLASK_ENV to development will enable debug mode
export FLASK_ENV=development

# We can run our server
flask run --host=0.0.0.0