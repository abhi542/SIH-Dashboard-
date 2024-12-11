
# from pymongo import MongoClient
# from schema import User  # Import the schema

# # MongoDB connection
# client = MongoClient("mongodb://admin:adminpassword@localhost:27017/")
# db = client["big_brains"]
# collection = db["user-data"]

# # Data to be inserted
# users_data = [
#     {
#         "user_id": "user123",
#         "username": "john_doe",
#         "language": "English",
#         "tasks": [
#             {
#                 "task_id": "task1",
#                 "task_name": "Help Old Lady Cross Road",
#                 "task_completed": True,
#                 "completion_time": "2024-12-03T12:00:00",
#                 "accuracy": 90,
#                 "feedback": "Good job! Keep helping."
#             }
#         ],
#         "metrics": {
#             "total_time_spent": 1200,
#             "correct_responses": 5,
#             "incorrect_responses": 2,
#             "average_accuracy": 85
#         },
#         "last_login": "2024-12-02T15:30:00"
#     },
#     {
#         "user_id": "user456",
#         "username": "jane_doe",
#         "language": "Spanish",
#         "tasks": [
#             {
#                 "task_id": "task2",
#                 "task_name": "Pick Up Trash at Park",
#                 "task_completed": False,
#                 "completion_time": None,
#                 "accuracy": None,
#                 "feedback": "Task pending."
#             }
#         ],
#         "metrics": {
#             "total_time_spent": 800,
#             "correct_responses": 4,
#             "incorrect_responses": 1,
#             "average_accuracy": 80
#         },
#         "last_login": "2024-12-02T14:00:00"
#     }
# ]

# # Validate and insert data
# for user_data in users_data:
#     try:
#         user = User(**user_data)  # Validate data using schema
#         collection.insert_one(user.model_dump())  # Insert into MongoDB
#         print(f"Inserted user: {user.user_id}")
#     except Exception as e:
#         print(f"Error inserting user: {e}")

# # Fetch and display all documents
# documents = collection.find()
# print("\nData in the collection:")
# for document in documents:
#     print(document)
# print("Documents written to Mongo Successfully!")

from pymongo import MongoClient
from schema import UserData  # Import the updated schema

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
    }
]

# Validate and insert data
for user_data in users_data:
    try:
        user = UserData(**user_data)  # Validate data using schema
        collection.insert_one(user.model_dump())  # Insert into MongoDB
        print(f"Inserted user: {user.user_id}")
    except Exception as e:
        print(f"Error inserting user: {e}")

# Fetch and display all documents
documents = collection.find()
print("\nData in the collection:")
for document in documents:
    print(document)
print("Documents written to Mongo Successfully!")

