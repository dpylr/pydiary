#!/usr/bin/env python3
from flask import Flask, render_template, redirect
from app.helpers import RegexConverter

from .planner import planner

BLUEPRINTS = (
    planner,
)


def add_custom_routing_converters(app):
    app.url_map.converters['regex'] = RegexConverter


def register_blueprints(app):
    for b in BLUEPRINTS:
        app.register_blueprint(b)


def configure_general(app):
    @app.route("/")
    def show_index():
        return redirect("planner")


def configure_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("layout/page_not_found.html"), 404


def configure_db(app):
    from app.database import db, init_db
    init_db(db, app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    add_custom_routing_converters(app)
    register_blueprints(app)
    configure_db(app)
    configure_general(app)
    configure_errors(app)

    return app

