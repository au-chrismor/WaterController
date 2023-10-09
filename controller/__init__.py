import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'control-data.db')
    )

    if test_config is None:
        # Load the instance config, if it exists when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/ping')
    def ping():
        return 'pong'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import day
    app.register_blueprint(day.bp)

    from . import controller
    app.register_blueprint(controller.bp)

    from . import port
    app.register_blueprint(port.bp)

    from . import sched
    app.register_blueprint(sched.bp)

    from . import status
    app.register_blueprint(status.bp)
    app.add_url_rule('/', endpoint='index')

    return app

