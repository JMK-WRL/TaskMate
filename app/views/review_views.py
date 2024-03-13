# app/views/review_views.py
from flask import Blueprint, render_template, request, jsonify
from app.models import Review

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify(reviews=[review.serialize() for review in reviews])

@review_bp.route('/review/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if review:
        return jsonify(review.serialize())
    else:
        return jsonify({'message': 'Review not found'}), 404

@review_bp.route('/review', methods=['POST'])
def create_review():
    data = request.get_json()
    new_review = Review(rating=data['rating'], comment=data['comment'])
    # Add additional fields as needed
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

# Add more routes and views as needed
