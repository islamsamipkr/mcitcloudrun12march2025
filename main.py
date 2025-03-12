from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/char_count", methods=["POST"])
def char_count():
    try:
        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing 'text' parameter"}), 400
        
        text = data["text"]
        count = len(text)
        
        return jsonify({"character_count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
