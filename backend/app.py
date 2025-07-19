# Import necessary libraries
import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import json
import random
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask application
# Crucially, tell Flask where to find the HTML templates
app = Flask(__name__, template_folder='../frontend')

# --- Configuration ---
# Get the NEW, secure API key from your environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
# Use the latest Gemini Flash model which is fast and efficient
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"


# --- Routes ---

# This route serves the main web page
@app.route('/')
def index():
    return render_template('index.html')

# This route handles the API logic
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    history = request.json.get('history', [])

    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    # Load intents from intents.json
    try:
        with open('backend/intents.json', 'r') as f:
            intents_data = json.load(f)
    except FileNotFoundError:
        return jsonify({'error': 'intents.json not found.'}), 500

    # Check for intent matches
    matched_intent_response = None
    for intent in intents_data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_message.lower():
                if intent['tag'] == 'time':
                    matched_intent_response = datetime.now().strftime("%I:%M %p")
                elif intent['tag'] == 'greeting':
                    matched_intent_response = random.choice(intent['responses'])
                break
        if matched_intent_response:
            break

    if matched_intent_response:
        return jsonify({'response': matched_intent_response})

    # If no intent matched, proceed with Gemini API
    if not GEMINI_API_KEY or "YOUR_GEMINI_API_KEY_HERE" in GEMINI_API_KEY:
        return jsonify({'error': 'API key is not configured. Please update .env and restart the server.'}), 500

    headers = {'Content-Type': 'application/json'}

    # Construct the full prompt with history
    full_prompt = ""
    # Add system instruction
    system_instruction = "You are a helpful and friendly assistant named 'Chip'. Always be cheerful and encouraging."
    full_prompt += f"System: {system_instruction}\n"

    if history:
        full_prompt += "Here is the conversation history:\n"
        for msg in history:
            full_prompt += f"{msg['sender'].capitalize()}: {msg['text']}\n"
        full_prompt += "\nNow, answer this question: "
    full_prompt += user_message

    data = {"contents": [{"parts": [{"text": full_prompt}]}]}

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()

        # --- THIS IS THE IMPROVEMENT ---
        # This is a safer way to get the text, preventing crashes if the format changes
        ai_message = response_json['candidates'][0]['content']['parts'][0]['text']

        return jsonify({'response': ai_message})

    except requests.exceptions.HTTPError as e:
        # This gives a more specific error for bad API keys or permissions
        return jsonify({'error': f'HTTP Error: {e}. Check if your API key is correct and has permissions.'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Network request failed: {e}'}), 500
    except (KeyError, IndexError):
        # This error often happens with an invalid API key
        return jsonify({'error': 'Invalid response from API. This is often caused by an incorrect or disabled API key.'}), 500

if __name__ == '__main__':
    # Use a different port like 5001 to avoid conflicts
    app.run(debug=True, port=5001)

