from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])

def root_path():
    return jsonify(msg="It's running!", code=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=43333)