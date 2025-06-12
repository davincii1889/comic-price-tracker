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

@@app.route("/ebay/delete-account-callback", methods=["POST"])
def ebay_delete_notification():
    # This must return the exact token string with a 200 status code
    return make_response("comicprice123tokenabc456def789ghi000jkl", 200)

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

