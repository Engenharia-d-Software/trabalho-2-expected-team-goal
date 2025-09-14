from sqlalchemy import nulls_last
from sqlalchemy.orm import Session

from model import Issue, TaskStep
from schemas import IssueCreate, IssueUpdate

from .crud import Crud


class CrudIssue(Crud[Issue, IssueCreate, IssueUpdate]):
    def __init__(self):
        super().__init__(Issue)

    def get_sorting_by_milestone(self, db: Session, task_step_id: int) -> list[Issue]:
        stmt = db.query(Issue)
        stmt = stmt.join(TaskStep).filter(Issue.task_step_id == task_step_id)
        return stmt.order_by(nulls_last(Issue.milestone)).all()
