from . import route_tableau
from flask import render_template

@route_tableau.route('tableauTime')
def tableauTime():
    return render_template('tableau/tableauTime.html')