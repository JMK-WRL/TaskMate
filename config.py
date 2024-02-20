import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True

    FIREBASE_CONFIG = {
        'apiKey': 'your_api_key',
        'authDomain': 'your_auth_domain',
        'projectId': 'your_project_id',
        'storageBucket': 'your_storage_bucket',
        'messagingSenderId': 'your_messaging_sender_id',
        'appId': 'your_app_id',
        'measurementId': 'your_measurement_id'
    }

    PAYPAL_CLIENT_ID = 'your_paypal_client_id'
    PAYPAL_CLIENT_SECRET = 'your_paypal_client_secret'
