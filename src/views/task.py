import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from control import issue
import model
from schemas import IssueCreate

def create_task(task_header: DeltaGenerator) -> bool:
    with task_header:
        task, description, createButton = st.columns(3, vertical_alignment="bottom")
        task_title = task.text_input("Nova tarefa")
        task_description = description.text_input("Descrição")
        clicked = createButton.button("Criar")

        if clicked:
            return issue.create_issue(
                IssueCreate(
                    title=task_title,
                    description=task_description,
                    task_step_id=1
                )
            )
        return None

def edite_issue(task_header: DeltaGenerator, db_tasks: list[model.TaskStep]):
    all_issues = [ issue for task in db_tasks for issue in task.issues]
    with task_header:
        issue_col, column_col, move_button_col = st.columns(3, vertical_alignment="bottom")

        selected_issue = issue_col.selectbox(
            "Selecione o issue",
            options=[issue for issue in all_issues],
            format_func=lambda i: i.title
        )

        selected_column = column_col.selectbox(
            "Selecione a coluna destino",
            options=[col for col in db_tasks],
            format_func=lambda c: c.name
        )

        if move_button_col.button("Mover"):
            issue.move_issue(selected_issue, selected_column)
            
            st.success(f"Issue '{selected_issue.title}' movido para '{selected_column.name}'")
            return True
        return False
