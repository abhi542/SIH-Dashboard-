from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Task metrics schema
class TaskMetrics(BaseModel):
    task_id: str
    completion_rate: float
    engagement_duration: int
    objects_identified: int
    companion_help_count: int

# Task schema
class Task(BaseModel):
    task_id: str
    task_name: str
    task_completed: bool
    completion_time: Optional[datetime] = None  # Optional completion time
    accuracy: Optional[int] = None  # Optional accuracy field
    feedback: Optional[str] = None  # Optional feedback
    metrics: TaskMetrics  # Task-specific metrics

# User schema
class UserData(BaseModel):
    user_id: str
    username: str
    language: str
    tasks: List[Task]
    metrics: dict  # Contains total_time_spent, correct_responses, incorrect_responses, and average_accuracy
    last_login: datetime
