from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)

from app.views import user_views, task_views, manager_views, payment_views, review_views

app.register_blueprint(user_views.user_bp)
app.register_blueprint(task_views.task_bp)
app.register_blueprint(manager_views.manager_bp)
app.register_blueprint(payment_views.payment_bp)
app.register_blueprint(review_views.review_bp)

with app.app_context():
    db.create_all()
