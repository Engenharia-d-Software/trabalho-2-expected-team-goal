import crud
import schemas

from . import _db_session

def ensure_created(task_step: schemas.TaskStepCreate):
    db_step = crud.task_step.get_by_name(_db_session, task_step.name)
    if db_step:
        return db_step
    return crud.task_step.create(_db_session, task_step)
