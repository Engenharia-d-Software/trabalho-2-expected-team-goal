import streamlit as st

from control import task_step
import model
import schemas

from views.kanban import render_kanban
from views.task import create_task, edite_issue


DEFAULT_COLUMN_NAMES = ["A Fazer", "Em Progresso", "Concluido"]
db_columns: list[model.TaskStep] = []

def header():
    headerText, crudTask = st.columns(2)

    with headerText:
        st.title("Quadro Kanban")

    return crudTask

if __name__ == "__main__":
    task_header = header()

    for column in DEFAULT_COLUMN_NAMES:
        db_task_step = task_step.ensure_created(schemas.TaskStepCreate(name=column))
        db_columns.append(db_task_step)
    create_task(task_header)
    edite_issue(task_header, db_columns)
    render_kanban(db_columns)
