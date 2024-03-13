# app/views/payment_views.py
from flask import Blueprint, render_template, request, jsonify
from app.models import Payment
from app import db

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify(payments=[payment.serialize() for payment in payments])

@payment_bp.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        return jsonify(payment.serialize())
    else:
        return jsonify({'message': 'Payment not found'}), 404

@payment_bp.route('/payment', methods=['POST'])
def create_payment():
    data = request.get_json()
    new_payment = Payment(amount=data['amount'], method=data['method'])
    # Add additional fields as needed
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment created successfully'}), 201

# Add more routes and views as needed
