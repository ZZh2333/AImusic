from . import route_tableau
from flask import render_template

@route_tableau.route('tableauPerson')
def tableauPerson():
    DWMC = '工会'
    return render_template('tableau/tableau.html',DWMC = DWMC)