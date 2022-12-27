import os
from flask import Flask, request
from revChatGPT import Chatbot
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_SESSION_KEY = os.getenv('OPEN_AI_SESSION_KEY')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gpt():
    data = request.get_json()
    chatbot = Chatbot({
        "session_token": OPEN_AI_SESSION_KEY  
    })
    response = chatbot.get_chat_response(data.get("message"), output="text")
    return response.get("message")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
