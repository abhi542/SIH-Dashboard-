# from pydantic import BaseModel, Field
# from typing import List, Optional
# from datetime import datetime

# class Task(BaseModel):
#     task_id: str
#     task_name: str
#     task_completed: bool
#     completion_time: Optional[datetime]
#     accuracy: Optional[int]
#     feedback: Optional[str]

# class Metrics(BaseModel):
#     total_time_spent: int
#     correct_responses: int
#     incorrect_responses: int
#     average_accuracy: float

# class UserData(BaseModel):
#     user_id: str
#     username: str
#     language: str
#     tasks: List[Task]
#     metrics: Metrics
#     last_login: Optional[datetime]


from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime

class Task(BaseModel):
    task_id: str
    task_name: str
    task_completed: bool
    completion_time: Optional[datetime] = None
    accuracy: Optional[int] = Field(None, ge=0, le=100)  # Ensure accuracy is between 0-100
    feedback: Optional[str] = None

    @validator("completion_time", pre=True)
    def parse_completion_time(cls, value):
        return datetime.fromisoformat(value) if value else None

class Metrics(BaseModel):
    total_time_spent: int = Field(..., gt=0)
    correct_responses: int = Field(..., ge=0)
    incorrect_responses: int = Field(..., ge=0)
    average_accuracy: int = Field(..., ge=0, le=100)

class User(BaseModel):
    user_id: str
    username: str
    language: str
    tasks: List[Task]
    metrics: Metrics
    last_login: datetime

    @validator("last_login", pre=True)
    def parse_last_login(cls, value):
        return datetime.fromisoformat(value)

    @validator("tasks", pre=True)
    def validate_tasks(cls, tasks):
        if not tasks:
            raise ValueError("Tasks list cannot be empty")
        return tasks
