from flask import Flask, request, Response
import openai
import os
from dotenv import load_dotenv 
load_dotenv()

app = Flask(__name__)

# Replace with your ChatGPT API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chatgpt-voice", methods=["GET", "POST"])  # Only path here
def chatgpt_voice():
    if request.method == "GET":
        return "✅ Flask app is live and reachable!"
    
    user_input = request.form.get("SpeechResult", "")
    print("User said:", user_input)

    # Use ChatGPT with context about EA Real Estate
    chat_response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a polite and helpful phone assistant for a company named EA Real Estate. Answer all questions professionally as their representative."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    bot_reply = chat_response.choices[0].message.content.strip()
    print("ChatGPT says:", bot_reply)

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>{bot_reply}</Say>
</Response>"""

    return Response(twiml, mimetype="text/xml")
