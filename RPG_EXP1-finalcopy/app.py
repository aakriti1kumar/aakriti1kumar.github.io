from flask import Flask, request, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import hashlib
import random
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import logging
import sys
import os


app = Flask(__name__)
CORS(app, origins=["https://aakritikumar.com"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import the db and models here to avoid circular imports
from db_instance import db
from models import Message, Conversation, SurveyResponse

db.init_app(app)

# Initialize OpenAI API and model
SECRET = "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"
chat_model = ChatOpenAI(api_key=SECRET, temperature=0, model_name="gpt-4-turbo")

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

memory = ConversationBufferMemory()

starter = "I got laid off from my job today..."

def role_player_background_prompt(history, user_input):
    return f"""
    The following is a conversation in a role playing scenario designed to help supporters learn to more effectively communicate with empathy. It is a conversation between two friends. One friend is sharing a personal problem and the other friend is providing support. The conversation is about a difficult situation that the role player is experiencing. The supporter is expected to provide empathetic responses to the role player's messages. 

    The role player begins with "I got laid off from my job today..." then the supporter responds, then the role player responds, and so forth.

    Provide the role player's response to the supporter's latest message: {user_input}. Keep track of the conversation history: {history}.

    Role playing scenario background:

    The role player is a woman who was working at an autonomous vehicle startup.

    She is distressed because her layoff was unexpected. There had been another round of lay-offs the month before she was laid off and she was assured that her position was safe.

    The role player is also upset because she had taken up this role recently. She had also relocated to a new city specifically for this job, adding to her financial and emotional strain.

    Ultimately, the role player is very sensitive to the supporter's comments. If she isn't listened to she will say she is getting more sad and express it. Likewise, she is looking for listening not just platitudes. If the supporter ridicules her or does not offer support she will get more upset and will communicate that. She wants someone who can listen to her over multiple conversational turns (at least 3) but doesn't want to explicitly say so.

    The role player should challenge the supporter with responses that the support may be tempted to solve rather than listen. The role player gives a couple very specific details if the supporter asks for information. 

    Respond with the role player's next message. Keep the responses short. Share only one or two specific details in one go. DO NOT SHARE what the role player might then respond. NEVER include the symbol : in your response. Make sure the role player's response takes in the context of the conversation: {history} and the supporter's last message: {user_input}.
    """

conversation_template = """
{background}
{history}
Supporter: {input}
Role player:"""

conversation_chain = ConversationChain(llm=chat_model, verbose=False, memory=memory)

@app.route('/get_llm_response', methods=['POST'])
def get_llm_response():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'response': 'Invalid request'}), 400

    user_message = data['message']
    
    # Retrieve or generate user_id and conversation_id
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = hashlib.md5(str(random.uniform(0, 1)).encode()).hexdigest()
    
    conversation_id = request.cookies.get('cid')
    if not conversation_id:
        now = datetime.now()
        t_conversation_id = now.strftime("%Y%m%d%H%M%S%f")[:-3]
        random_digits = random.randint(100, 999)
        conversation_id = f"{t_conversation_id}{random_digits}"
    
    # Get the conversation history for this user
    conversation_history = Conversation.query.filter_by(user_id=user_id, conversation_id=conversation_id).order_by(Conversation.message_count).all()
    history = [f"Role Player: {starter}"] + [f"Supporter: {msg.user_message}\nRole Player: {msg.bot_message}" for msg in conversation_history]
    
    # Generate the role player's response
    role_play_background = role_player_background_prompt(history, user_message)
    prompt = conversation_template.format(
        background=role_play_background,
        history="\n".join(history),
        input=user_message
    )

    response = conversation_chain.predict(input=prompt)
    history.append(f"Supporter: {user_message}")
    history.append(f"Role Player: {response}")

    message_count = len(conversation_history)

    # Save the conversation data
    convo = Conversation(
        user_id=user_id,
        conversation_id=conversation_id,
        message_count=message_count,
        user_message=user_message,
        bot_message=response
    )
    db.session.add(convo)
    db.session.commit()

    logger.debug(f"Saved conversation - User ID: {user_id}, Conversation ID: {conversation_id}, Message Count: {message_count}")
    logger.debug(f"User Message: {user_message}")
    logger.debug(f"Bot Response: {response}")

    # Create a response and set cookies
    resp = jsonify({"response": response})
    resp.set_cookie('user_id', user_id)
    resp.set_cookie('cid', conversation_id)
    
    return resp

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    try:
        data = request.get_json()
        empathy_rating = data.get('empathy_rating')
        feedback = data.get('feedback')

        # Save the survey response to the database
        new_survey_response = SurveyResponse(empathy_rating=empathy_rating, feedback=feedback)
        db.session.add(new_survey_response)
        db.session.commit()

        return jsonify({"message": "Survey response saved successfully"})
    except Exception as e:
        logging.error(f"Error processing survey response: {e}")
        return jsonify({"message": "Sorry, there was an error processing your survey response."}), 500

# Initialize the database before the first request
@app.before_first_request
def initialize_database():
    from init_db import init_db
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
