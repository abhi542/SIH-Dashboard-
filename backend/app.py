from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://admin:adminpassword@localhost:27017/")
db = client["big_brains"]
collection = db["user-data"]

@app.route("/")
def home():
    """Render the dashboard with user data."""
    users = list(collection.find())
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string for JSON compatibility
    return render_template("dashboard.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)