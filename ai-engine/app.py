from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, jsonify
import google.generativeai as genai
import re
from flask_cors import CORS

# ----------------------------
# Flask app setup
# ----------------------------
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "https://ai-bug-fix-suggestion-tool-1.onrender.com",
    "https://690e476b80833010e0e46a5e--ai-bug-fix.netlify.app"
]}})

# ----------------------------
# Gemini API setup
# ----------------------------
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in environment variables")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# /analyze endpoint
# ----------------------------
@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json(force=True)
    code = data.get('code', '')

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Optimized prompt for LLM
    prompt = f"""
You are an expert developer. Analyze the following code and return output in **strictly** this format.
Do NOT add explanations outside this format. Always fill in the fixed code.

🛠️ Issues:
- (list actual issues found in the code)

💡 Suggestions:
- (list practical suggestions to fix the code)

🔧 Fixed Code:

Code to analyze:
{code}
"""

    try:
        # Call Gemini model
        response = model.generate_content(prompt=prompt)
        content = response.text

        print("--- LLM Output ---\n", content)

        # Extract issues, suggestions, fixed code using regex
        issues_match = re.search(r"🛠️ Issues:\s*(.*?)(?:\n\n|💡 Suggestions:)", content, re.DOTALL)
        suggestions_match = re.search(r"💡 Suggestions:\s*(.*?)(?:\n\n|🔧 Fixed Code:)", content, re.DOTALL)
        fixed_code_match = re.search(r"🔧 Fixed Code:\s*```(?:\w+)?\n([\s\S]*?)```", content)

        issues = [i.strip("- ").strip() for i in issues_match.group(1).split("\n") if i.strip()] if issues_match else []
        suggestions = [s.strip("- ").strip() for s in suggestions_match.group(1).split("\n") if s.strip()] if suggestions_match else []
        fixed_code = fixed_code_match.group(1).strip() if fixed_code_match else ""

        return jsonify({
            "issues": issues,
            "suggestions": suggestions,
            "fixedCode": fixed_code
        })

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

# ----------------------------
# Run Flask app
# ----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
