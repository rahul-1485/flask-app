from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, CI/CD!"


@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


@app.route("/subtract", methods=["GET"])
def subtract_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a - b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


# ✅ NEW: multiply route
@app.route("/multiply", methods=["GET"])
def multiply_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a * b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(debug=True)
