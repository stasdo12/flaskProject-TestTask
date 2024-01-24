from flask import Flask
from flask_restful import Api
from resources import ProductResource
from config import Config
from database import db, cache
import pandas as pd


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)
    api.add_resource(ProductResource, '/product/<int:product_id>', '/product/<int:product_id>/review',
                     '/product/<int:product_id>/review/<int:comment_id>')

    with app.app_context():
        db.init_app(app)
        cache.init_app(app)
        initialize_database()

    return app


def initialize_database():
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


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
