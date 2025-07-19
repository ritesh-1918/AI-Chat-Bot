import os
import requests
from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../public', static_url_path='')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # ... (the rest of your send_message function remains the same)
    user_message = request.json.get('message')
    function_type = request.json.get('function')

    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    if not GEMINI_API_KEY or "YOUR_GEMINI_API_KEY_HERE" in GEMINI_API_KEY:
        return jsonify({'error': 'API key is not configured on the server.'}), 500

    prompt = ""
    if function_type == 'summarize':
        prompt = f"Please provide a clear and concise summary of the following text:\n\n---\n{user_message}\n---"
    elif function_type == 'creative':
        prompt = f"Generate a short, creative piece of writing (like a poem or a micro-story) inspired by the following topic: '{user_message}'"
    else:
        prompt = user_message

    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        ai_message = response_json['candidates'][0]['content']['parts'][0]['text']
        return jsonify({'response': ai_message})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
        
# ... (your log_feedback function remains the same)
@app.route('/log_feedback', methods=['POST'])
def log_feedback():
    data = request.json
    print(f"Feedback received: {data}")
    return jsonify({'status': 'success'})

