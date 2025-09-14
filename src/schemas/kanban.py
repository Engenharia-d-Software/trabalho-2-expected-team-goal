from datetime import datetime

from pydantic import BaseModel, Field


class IssueCreate(BaseModel):
    title: str
    description: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    milestone: datetime | None = None
    task_step_id: int


class IssueUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    created_at: datetime | None = None
    milestone: datetime | None = None
    task_step_id: int | None = None


class TaskStepCreate(BaseModel):
    name: str
    wip_limit: int | None = None


class TaskStepUpdate(BaseModel):
    name: str | None = None
    wip_limit: int | None = None
