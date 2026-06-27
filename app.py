script_content = """import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    user_idea = request.form.get('idea')
    prompt = f"Act as a professional startup incubator mentor. Critically evaluate this business concept. Provide its Strengths, Target Market Demographics, Potential Risks, and a final viability rating out of 10:\\n\\n{user_idea}"
    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        return jsonify({'evaluation': response.text})
    except Exception as e:
        return jsonify({'evaluation': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(script_content)

print("Standalone app.py file generated in your folder. Upload this file and the 'templates' folder straight to GitHub!")
