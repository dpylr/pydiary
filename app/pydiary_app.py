#!/usr/bin/env python3
from flask import Flask, render_template, request
from app.helpers import RegexConverter

from .tasks import tasks
from .diary import diary
from .virtues import virtues
from .auth import auth
from .planner import planner

BLUEPRINTS = (
    tasks,
    diary,
    virtues,
    planner,
    auth
)


def add_custom_routing_converters(app):
    app.url_map.converters['regex'] = RegexConverter


def register_blueprints(app):
    for b in BLUEPRINTS:
        app.register_blueprint(b)


def configure_general(app):
    @app.route("/")
    def show_index():
        return render_template('index.html')


def configure_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("layout/page_not_found.html"), 404

    @app.errorhandler(403)
    def page_forbidden(error):
        return render_template("layout/page_not_found.html"), 403


def configure_db(app):
    from app.database import db, init_db
    init_db(db, app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()


def configure_extensions(app):
    from app.extensions import init_extensions
    init_extensions(app)


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    add_custom_routing_converters(app)
    register_blueprints(app)
    configure_db(app)
    configure_extensions(app)
    configure_general(app)
    configure_errors(app)

    return app

