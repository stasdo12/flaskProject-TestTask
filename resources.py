from flask import jsonify, request
from flask_restful import Resource

from models import Product, Review
from database import db, cache


class ProductResource(Resource):
    @staticmethod
    @cache.memoize(timeout=60)
    def get(product_id):
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404

        product_info = {
            'asin': product.asin,
            'title': product.title
        }

        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        reviews = Review.query.filter_by(asin=product.asin).paginate(page=page, per_page=per_page, error_out=False)

        reviews_list = []
        for review in reviews.items:
            review_data = {
                'ReviewTitle': review.title,
                'ReviewText': review.review
            }
            reviews_list.append(review_data)

        result = {
            'ProductInfo': product_info,
            'Reviews': reviews_list,
            'Pagination': {
                'page': page,
                'per_page': per_page,
                'total_pages': reviews.pages,
                'total_items': reviews.total
            }
        }

        return jsonify(result)

    @staticmethod
    def validate_data(data):
        if 'title' not in data or 'review' not in data:
            return {'message': 'Missing required fields (title or review)'}, 400
        return data

    @staticmethod
    def put(product_id):
        try:
            data = request.get_json()
            data = ProductResource.validate_data(data)
            if data is not None:
                product = Product.query.get(product_id)
                if not product:
                    return {'message': 'Product not found'}, 404

                if 'title' in data and 'review' in data:
                    new_review = Review(title=data['title'], review=data['review'], asin=product.asin)
                else:
                    return {'message': 'Missing required fields (title or review)'}, 400

                db.session.add(new_review)
                db.session.commit()

                cache.delete_memoized(ProductResource.get, product_id=product_id)

                return {'message': 'Review added successfully'}, 201
        except Exception as e:
            print(f"An error occurred: {e}")
            return {'message': 'Internal Server Error'}, 500
