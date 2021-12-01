from application import app
from web.controllers.index import route_index
from web.controllers.static import route_static

from web.controllers.index import route_index


app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_static, url_prefix="/static")


from web.controllers.tableau import route_tableau
app.register_blueprint(route_tableau,url_prefix="/tableau")