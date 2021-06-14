import os
from flask import Flask
from tri_test.db import db


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    if test_config:
        app.config.from_object(test_config)
    else:
        env_config = os.getenv("APP_SETTINGS", "tri_test.config.DevConfig")
        print(f'Using config from {env_config}.')
        app.config.from_object(env_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    db.create_all(app=app)

    # Register app endpoints
    from tri_test import message
    app.register_blueprint(message.bp)
    app.add_url_rule('/', endpoint='index')

    # Register simple test endpoint, just for having at least one endpoint to hit.
    @app.route('/version')
    def hello():
        return '1.0.0'  # hardcoded for now

    return app


# For debug purposes only
if __name__ == '__main__':
    app_instance = create_app()
    app_instance.run(debug=True)
