from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Comic Price Tracker!"

@app.route("/deletion-notify", methods=["POST"])
def deletion_notify():
    return "Account deletion notice received", 200

if __name__ == "__main__":
    app.run(debug=True)
