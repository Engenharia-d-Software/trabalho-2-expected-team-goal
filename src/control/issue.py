from sqlalchemy.exc import IntegrityError

import crud
import model
from schemas import IssueCreate, IssueUpdate

from . import _db_session

def create_issue(issue: IssueCreate):
    try:
        return crud.issue.create(_db_session, issue)
    except IntegrityError:
        raise ValueError("The issue name should be unique")


def update_issue(issue: IssueUpdate):
    try:
        crud.issue.update(_db_session, issue)
    except IntegrityError:
        raise ValueError("The issue name should be unique")

def move_issue(db_issue: model.Issue, to_task_step: model.TaskStep):
    crud.issue.update(
        _db_session,
        db_obj=db_issue,
        db_in=IssueUpdate(
            task_step_id=to_task_step.id
        )
    )
