from database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    asin = db.Column(db.String(10), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='product', lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    review = db.Column(db.Text, nullable=False)
    asin = db.Column(db.String(10), db.ForeignKey('product.asin'), nullable=False)
