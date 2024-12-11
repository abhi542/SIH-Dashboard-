from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://admin:adminpassword@localhost:27017/")
db = client["big_brains"]
collection = db["user-data"]

# Function to get user data based on user_id
def get_user_by_id(user_id):
    user_data = collection.find_one({"user_id": user_id})
    
    if user_data:
        # Calculate KPIs
        kpis = calculate_kpis(user_data)
        user_data["kpis"] = kpis
        return user_data
    else:
        return None

# Function to calculate KPIs for a user
def calculate_kpis(user_data):
    total_tasks = len(user_data["tasks"])
    completed_tasks = 0
    total_accuracy = 0
    total_time_spent = 0
    correct_responses = 0
    incorrect_responses = 0
    engagement_duration = 0
    companion_help_count = 0

    for task in user_data["tasks"]:
        if task["task_completed"]:
            completed_tasks += 1
            total_accuracy += task["accuracy"] if task["accuracy"] else 0
            total_time_spent += task["metrics"]["engagement_duration"]
            correct_responses += 1
            engagement_duration += task["metrics"]["engagement_duration"]
            companion_help_count += task["metrics"]["companion_help_count"]
        else:
            incorrect_responses += 1

    # Calculate KPIs
    task_completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    average_accuracy = total_accuracy / completed_tasks if completed_tasks > 0 else 0
    total_engagement_duration = engagement_duration
    correct_vs_incorrect = (correct_responses, incorrect_responses)
    average_time_per_task = total_time_spent / total_tasks if total_tasks > 0 else 0

    # Last login recency
    last_login = datetime.strptime(user_data["last_login"], "%Y-%m-%dT%H:%M:%S")
    current_time = datetime.now()
    time_since_last_login = (current_time - last_login).days

    # Return KPIs
    kpis = {
        "task_completion_rate": task_completion_rate,
        "average_accuracy": average_accuracy,
        "total_engagement_duration": total_engagement_duration,
        "correct_vs_incorrect": correct_vs_incorrect,
        "average_time_per_task": average_time_per_task,
        "time_since_last_login": time_since_last_login
    }
    return kpis

# Route to ask for user ID input
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_id = request.form['user_id']
        return redirect(url_for('dashboard', user_id=user_id))
    return render_template('home.html')

# Route to display the dashboard for a specific user
@app.route('/dashboard', methods=['GET'])
def dashboard():
    user_id = request.args.get('user_id')  # Get user_id from the query parameter
    if user_id:
        user = get_user_by_id(user_id)  # Fetch the user data
        if user:
            return render_template('dashboard.html', user=user)  # Pass user data to HTML
        else:
            return "User ID not provided", 400

            
    else:
        return "User ID not provided", 400

if __name__ == '__main__':
    app.run(debug=True)
