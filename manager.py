from logging import debug
from application import app, manager
import traceback
import sys
from flask_script import Server
import www


manager.add_command("runserver", Server(
    host="0.0.0.0", port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
