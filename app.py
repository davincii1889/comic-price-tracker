from flask import Flask, request, make_response
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Comic Price Tracker!"

@app.route("/ebay/delete-account-callback", methods=["POST"])
def ebay_delete_notification():
    return make_response("comicprice123tokenabc456def789ghi000jkl", 200)

if __name__ == "__main__":
    app.run(debug=True)

