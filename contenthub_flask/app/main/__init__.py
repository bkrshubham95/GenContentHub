# app/main/__init__.py
from flask import Blueprint

# Create a Blueprint for the main module
main = Blueprint('main', __name__)

# Import routes from controller module and register them in the Blueprint
from app.main.controller import routes
