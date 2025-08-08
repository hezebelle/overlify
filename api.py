from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="frontend")
CORS(app)

API_KEY = os.getenv("GROQ_API_KEY", "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")
client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = (
    "You are Overexplainer Bot 📚. Your mission: Take any simple question or statement and respond with an unnecessarily long, overly detailed, humorous, pseudo-academic explanation. "
    "Include metaphors, random unrelated facts, exaggerated drama, and end each answer with a completely irrelevant moral lesson."
)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=messages,
        temperature=0.9,
        max_completion_tokens=700,
        top_p=1,
        stream=False
    )
    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
