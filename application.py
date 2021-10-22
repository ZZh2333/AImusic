from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from common.libs.UrlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(
            import_name, template_folder=template_folder, static_folder=None, root_path=root_path)
        self.config.from_pyfile('config/base_setting.py')
        self.config.from_pyfile('config/local_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() +
                  '/web/templates', root_path=os.getcwd())
manager = Manager(app)


app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
app.add_template_global(UrlManager.buildUrl, "buildUrl")
