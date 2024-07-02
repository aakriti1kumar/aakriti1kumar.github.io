from db_instance import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(256))
    llm_response = db.Column(db.String(256))

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True)
    conversation_id = db.Column(db.String(64), index=True)
    message_count = db.Column(db.Integer)
    user_message = db.Column(db.String(256))
    bot_message = db.Column(db.String(256))
    time_created = db.Column(db.DateTime, default=db.func.now())

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empathy_rating = db.Column(db.String(50), nullable=False)
    feedback = db.Column(db.Text, nullable=True)
