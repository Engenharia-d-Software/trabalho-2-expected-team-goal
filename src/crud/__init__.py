from model import Base

from .crud_task_step import CrudTaskStep
from .crud_issue import CrudIssue
from ._db import create_all, get_session

task_step = CrudTaskStep()
issue = CrudIssue()
create_all(Base)


__all__ = [
    "get_session"
]
