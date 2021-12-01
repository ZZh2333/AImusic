from flask import Blueprint,render_template

route_tableau = Blueprint("tableau_page",__name__)

from .tableauPerson import *
from .tableauTime import *

@route_tableau.route('/')
def tableau():
    return "Tableau Page"