import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")

app = Flask(__name__)

# Function to send user queries to Google AI Chatbot
def chat_with_pharmaverse(user_input):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GOOGLE_AI_API_KEY}
    
    data = {
        "contents": [{"parts": [{"text": f'PharmaVerse assistant response: {user_input}'}]}]
    }

    response = requests.post(url, headers=headers, params=params, json=data)
    response_json = response.json()
    return response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chat_with_pharmaverse(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
