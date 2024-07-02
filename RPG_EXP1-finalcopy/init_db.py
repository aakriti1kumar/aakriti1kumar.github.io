from db_instance import db
from models import Message, Conversation, SurveyResponse
from flask import Flask

def init_db():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()
