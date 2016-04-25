#!/usr/bin/env python3
from app.database import db_session, init_db
from flask import Flask, render_template, redirect

from .planner import planner

BLUEPRINTS = (
    planner,
)


def register_blueprints(app):
    for b in BLUEPRINTS:
        app.register_blueprint(b)
    return app


def configure_general(app):
    @app.route("/")
    def show_index():
        return redirect("planner")


def configure_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("layout/page_not_found.html"), 404


def configure_db(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()



def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    configure_general(app)
    configure_errors(app)
    configure_db(app)
    app.config.from_object('config')
    return app


app = create_app()