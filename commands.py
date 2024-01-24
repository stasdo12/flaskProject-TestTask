import click
from flask import current_app
from flask.cli import with_appcontext
import app
from database import db


@click.command("init-db")
@with_appcontext
def init_db():
    db.init_app(current_app)
    with current_app.app_context():
        app.initialize_database()
        click.echo("Database initialized and populated with data.")
