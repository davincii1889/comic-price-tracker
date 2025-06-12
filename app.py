from flask import Flask, request, make_response
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Optional: Secret key for sessions (if needed)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")

# Home route
@app.route("/")
def home():
    return "Welcome to Comic Price Tracker!"

# eBay Account Deletion Notification verification route

@app.route("/ebay/delete-account-callback", methods=["GET", "POST", "HEAD", "OPTIONS", "PUT"])
def ebay_delete_notification():
    # Return token as plain text
    resp = make_response("comicprice123tokenabc456def789ghi000jkl", 200)
    resp.mimetype = "text/plain"
    return resp

# Placeholder for a future route to fetch comic prices
@app.route("/api/comics")
def get_comic_prices():
    return {
        "status": "success",
        "message": "This route will fetch comic prices from eBay."
    }

# Run the app (for local development)
if __name__ == "__master__":
    app.run(debug=True)

