from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template for input form
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Character Counter</title>
</head>
<body>
    <h2>Enter a string to count characters:</h2>
    <form action="/char_count" method="post">
        <input type="text" name="text" required>
        <button type="submit">Submit</button>
    </form>
    {% if result is not none %}
        <h3>Character Count: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_FORM, result=None)

@app.route("/char_count", methods=["POST"])
def char_count():
    try:
        text = request.form.get("text")  # Get input from form
        if not text:
            return render_template_string(HTML_FORM, result="Error: No text provided")
        
        count = len(text)
        return render_template_string(HTML_FORM, result=count)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
