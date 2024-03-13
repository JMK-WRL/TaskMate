# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    FIREBASE_CONFIG = {
        'apiKey': os.environ.get('FIREBASE_API_KEY') or 'your_api_key',
        'authDomain': os.environ.get('FIREBASE_AUTH_DOMAIN') or 'your_auth_domain',
        'projectId': os.environ.get('FIREBASE_PROJECT_ID') or 'your_project_id',
        'storageBucket': os.environ.get('FIREBASE_STORAGE_BUCKET') or 'your_storage_bucket',
        'messagingSenderId': os.environ.get('FIREBASE_MESSAGING_SENDER_ID') or 'your_messaging_sender_id',
        'appId': os.environ.get('FIREBASE_APP_ID') or 'your_app_id',
        'measurementId': os.environ.get('FIREBASE_MEASUREMENT_ID') or 'your_measurement_id'
    }

    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID') or 'your_paypal_client_id'
    PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET') or 'your_paypal_client_secret'
