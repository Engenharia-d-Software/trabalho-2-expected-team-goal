from sqlalchemy.orm import Session

from model import TaskStep
from schemas import TaskStepCreate, TaskStepUpdate

from .crud import Crud

class CrudTaskStep(Crud[TaskStep, TaskStepCreate, TaskStepUpdate]):
    def __init__(self):
        super().__init__(TaskStep)

    def get_by_name(self, db: Session, name: str) -> TaskStep | None:
        stmt = db.query(TaskStep)
        stmt = stmt.filter(TaskStep.name == name)
        return stmt.first()
