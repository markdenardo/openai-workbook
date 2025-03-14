from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Test route to verify backend is working
@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    
    # For now, just echo the message back
    response = f"Server received: {message}"
    
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)