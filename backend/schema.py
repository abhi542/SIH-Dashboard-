

from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime


class UserMetrics(BaseModel):
    total_time_spent: int
    correct_responses: int
    incorrect_responses: int
    average_accuracy: float = Field(..., ge=0, le=100)

    @validator("total_time_spent", "correct_responses", "incorrect_responses", pre=True)
    def non_negative_values(cls, value):
        if value < 0:
            raise ValueError("Metrics values must be non-negative")
        return value


class TaskMetrics(BaseModel):
    task_id: str
    completion_rate: float = Field(..., ge=0.0, le=100.0)
    engagement_duration: int = Field(..., gt=0)
    objects_identified: int = Field(..., ge=0)
    companion_help_count: int = Field(..., ge=0)

    @validator("task_id")
    def task_id_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Task ID must not be empty")
        return value


class Task(BaseModel):
    task_id: str
    task_name: str
    task_completed: bool
    completion_time: Optional[datetime]
    accuracy: Optional[int] = Field(None, ge=0, le=100)
    feedback: Optional[str] = None
    metrics: TaskMetrics

    @validator("completion_time", pre=True)
    def parse_completion_time(cls, value):
        return datetime.fromisoformat(value) if value else None

    @validator("task_name")
    def task_name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Task name must not be empty")
        return value


class UserData(BaseModel):
    user_id: str
    username: str
    language: str
    tasks: List[Task]
    metrics: UserMetrics
    last_login: Optional[datetime]

    @validator("last_login", pre=True)
    def parse_last_login(cls, value):
        return datetime.fromisoformat(value) if value else None

    @validator("tasks", pre=True)
    def validate_tasks(cls, tasks):
        if not tasks:
            raise ValueError("Tasks list cannot be empty")
        return tasks

    @validator("user_id", "username", "language")
    def string_fields_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("String fields must not be empty")
        return value
