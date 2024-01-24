import click
from flask import current_app
from flask.cli import with_appcontext
from database import db
import pandas as pd


@click.command("init-db")
@with_appcontext
def init_db():
    db.init_app(current_app)
    with current_app.app_context():
        db.drop_all()
        db.create_all()
        products_df = pd.read_csv('static/data/Products.csv')
        products_df.columns = ['title', 'asin']

        reviews_df = pd.read_csv('static/data/Reviews.csv')
        reviews_df.columns = ['asin', 'title', 'review']

        products_df.to_sql('product', con=db.engine, if_exists='append', index=False,
                           dtype={'title': db.String(255), 'asin': db.String(10)})

        reviews_df.to_sql('review', con=db.engine, if_exists='append', index=False,
                          dtype={'asin': db.String(10), 'title': db.String(255), 'review': db.Text})

        click.echo("Database initialized and populated with data.")
