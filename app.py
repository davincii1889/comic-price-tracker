from flask import Flask, request
from dotenv import load_dotenv
import os

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

@app.route("/ebay/delete-account-callback", methods=["POST"])
def ebay_delete_notification():
    return "comicprice123tokenabc456def789ghi000jkl", 200

# Placeholder for a future route to fetch comic prices
@app.route("/api/comics")
def get_comic_prices():
    return {
        "status": "success",
        "message": "This route will fetch comic prices from eBay."
    }

# Run the app (for local development)
if __name__ == "__main__":
    app.run(debug=True)

