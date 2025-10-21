# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import json

app = Flask(__name__)
CORS(app)

def solve_questions(data):
    out = []
    questions = data.get("questions", [])
    for q in questions:
        question_text = q.get("question", "")
        options = [q.get(f"option{i}", "") for i in range(1,5)]
        hashed = q.get("answer", "")
        correct = None
        # ensure hashed is bytes
        try:
            hashed_b = hashed.encode('utf-8')
            for opt in options:
                if not opt:
                    continue
                if bcrypt.checkpw(opt.encode('utf-8'), hashed_b):
                    correct = opt
                    break
        except Exception as e:
            correct = f"Error checking answer: {str(e)}"
        out.append({
            "question": question_text,
            "options": options,
            "correct": correct
        })
    return out

@app.route("/api/solve", methods=["POST"])
def api_solve():
    """
    Accepts:
    - JSON body (application/json) with the content of questions.json
    OR
    - multipart/form-data with a file field "file" containing questions.json
    Returns:
    - JSON list of results [{"question":..., "options":[...], "correct":...}, ...]
    """
    try:
        # file upload (form)
        if "file" in request.files:
            f = request.files["file"]
            data = json.load(f)
        else:
            data = request.get_json(force=True)
        results = solve_questions(data)
        return jsonify({"ok": True, "results": results})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400

if __name__ == "__main__":
    # run: python app.py
    app.run(debug=True, port=5000)
