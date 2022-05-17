from flask import Flask

app = Flask(__name__)

@app.route("/", method=["GET"])

def root_path():
    return jsonfy(msg="It's running!", code=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=43333)