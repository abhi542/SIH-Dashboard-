


from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://admin:adminpassword@localhost:27017/")
db = client["big_brains"]
collection = db["user-data"]

# Data to be inserted
users_data = [
    {
        "user_id": "user123",
        "username": "john_doe",
        "language": "English",
        "tasks": [
            {
                "task_id": "task1",
                "task_name": "Help Old Lady Cross Road",
                "task_completed": True,
                "completion_time": "2024-12-03T12:00:00",
                "accuracy": 90,
                "feedback": "Good job! Keep helping.",
                "metrics": {
                    "task_id": "task1",
                    "completion_rate": 95.0,
                    "engagement_duration": 300,
                    "objects_identified": 10,
                    "companion_help_count": 2
                }
            }
        ],
        "metrics": {
            "total_time_spent": 1200,
            "correct_responses": 5,
            "incorrect_responses": 2,
            "average_accuracy": 85.5
        },
        "last_login": "2024-12-02T15:30:00"
    },
    {
        "user_id": "user456",
        "username": "jane_doe",
        "language": "Spanish",
        "tasks": [
            {
                "task_id": "task2",
                "task_name": "Pick Up Trash at Park",
                "task_completed": False,
                "completion_time": None,
                "accuracy": None,
                "feedback": "Task pending.",
                "metrics": {
                    "task_id": "task2",
                    "completion_rate": 50.0,
                    "engagement_duration": 150,
                    "objects_identified": 5,
                    "companion_help_count": 1
                }
            }
        ],
        "metrics": {
            "total_time_spent": 800,
            "correct_responses": 4,
            "incorrect_responses": 1,
            "average_accuracy": 80.0
        },
        "last_login": "2024-12-02T14:00:00"
    },
    # Add more user data records...
]

# Insert users data into MongoDB collection
for user in users_data:
    collection.insert_one(user)

# Function to calculate KPIs for each user
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

    # Task Completion Rate
    task_completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Average Task Accuracy
    average_accuracy = total_accuracy / completed_tasks if completed_tasks > 0 else 0

    # Engagement Duration (Total Time Spent)
    total_engagement_duration = engagement_duration

    # Completion Rate for Each Task
    completion_rate_for_each_task = []
    for task in user_data["tasks"]:
        if task["task_completed"]:
            task_completion_rate_for_task = (task["metrics"]["completion_rate"])
            completion_rate_for_each_task.append(task_completion_rate_for_task)

    # Correct vs Incorrect Responses
    correct_vs_incorrect = (correct_responses, incorrect_responses)

    # Average Time Per Task
    average_time_per_task = total_time_spent / total_tasks if total_tasks > 0 else 0

    # Last Login Recency
    last_login = datetime.strptime(user_data["last_login"], "%Y-%m-%dT%H:%M:%S")
    current_time = datetime.now()
    time_since_last_login = (current_time - last_login).days

    # Final KPIs
    kpis = {
        "task_completion_rate": task_completion_rate,
        "average_accuracy": average_accuracy,
        "total_engagement_duration": total_engagement_duration,
        "correct_vs_incorrect": correct_vs_incorrect,
        "average_time_per_task": average_time_per_task,
        "time_since_last_login": time_since_last_login
    }

    return kpis
