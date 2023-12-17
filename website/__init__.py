from flask import Flask, render_template, request, blueprints, jsonify
import os
from flask_executor import Executor


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY="dev",
    #     DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    # )

    from flask_bootstrap import Bootstrap5

    Bootstrap5(app)

    app.config["TEMPLATES_AUTO_RELOAD"] = True
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # routes

    @app.route("/")
    def index():
        return render_template("index.html.j2")

    @app.route("/tools")
    def tools():
        return render_template("tools.html.j2")

    # if __name__ == "__main__":
    #     app.run(debug=True)

    return app
