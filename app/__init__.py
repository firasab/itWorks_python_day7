# __init__.py
import flask


app = flask.Flask(__name__) # __name__ is the name of the folder


from . import views