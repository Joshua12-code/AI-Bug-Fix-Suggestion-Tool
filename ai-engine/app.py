from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, jsonify
import google.generativeai as genai
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://ai-bug-fix-suggestion-tool-1.onrender.com"}})

# ✅ Configure Gemini API Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# ✅ Use latest Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data.get('code')
    language = data.get('language')

    prompt = f"""
    Analyze this {language} code and return ONLY in the following format:

    🛠️ Issues:
    - issue 1
    - issue 2

    💡 Suggestions:
    - suggestion 1
    - suggestion 2

    🔧 Fixed Code:
    ```java
    // fixed code here
    ```

    Code:
    {code}
    """

    try:
        # ✅ Correct API call for latest SDK
        response = model.generate_content(prompt)
        content = response.text

        print("--- LLM Output ---\n", content)

        issues_match = re.search(r"🛠️ Issues:\s*(.*?)(?:\n\n|💡 Suggestions:)", content, re.DOTALL)
        suggestions_match = re.search(r"💡 Suggestions:\s*(.*?)(?:\n\n|🔧 Fixed Code:)", content, re.DOTALL)
        fixed_code_match = re.search(r"🔧 Fixed Code:\s*```(?:java)?\n([\s\S]*?)```", content)

        issues = issues_match.group(1).strip().split("\n") if issues_match else []
        suggestions = suggestions_match.group(1).strip().split("\n") if suggestions_match else []
        fixed_code = fixed_code_match.group(1).strip() if fixed_code_match else ""

        return jsonify({
            "issues": issues,
            "suggestions": suggestions,
            "fixedCode": fixed_code
        })

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # ✅ Important for Render or any cloud hosting
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
