from sqlalchemy.exc import IntegrityError

import crud
from schemas import IssueCreate, IssueUpdate

from src.model import Issue


def create_issue(issue: IssueCreate):
    try:
        return crud.issue.create(issue)
    except IntegrityError:
        raise ValueError("The issue name should be unique")


def update_issue(issue: IssueUpdate):
    try:
        crud.issue.update(issue)
    except IntegrityError:
        raise ValueError("The issue name should be unique")

