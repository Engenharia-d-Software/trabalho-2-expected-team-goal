import uuid
import streamlit as st
import streamlit_shadcn_ui as ui

from control import task_step
from control import issue

import model
import schemas

st.set_page_config(layout="wide")


def header():
    headerText, crudTask = st.columns(2)

    with headerText:
        st.title("Quadro Kanban")
        st.subheader("Gerencie suas tarefas de forma visual")
        st.markdown("Organize seu fluxo de trabalho de maneira simples e eficiente :pushpin:")

    return crudTask


def column_title(column, title):
    with column:
        st.header(title)

def create_task(crud_colunm):
    with crud_colunm:
        task, description, createButton = st.columns(3, vertical_alignment="bottom")
        task_title = task.text_input("Nova tarefa")
        task_description = description.text_input("Descrição")
        clicked = createButton.button("Criar")

        if clicked:
            return task_title,task_description
        return None

def add_card(column, issue: model.Issue):
    # Exemplo de card com imagem, título, texto e estilos personalizados
    with column:
        with ui.card(key=str(uuid.uuid4())):
            ui.element(
                "span",
                children=[issue.title],
                className="text-gray-400 text-sm font-medium m-1",
                key="label1",
            )


if __name__ == "__main__":
    crud_task_col = header()
    task_data = create_task(crud_task_col)

    if task_data:
        created_task = issue.create_issue(task_data)
        st.write(task_data)

    DEFAULT_COLUMN_NAMES = ["A Fazer", "Em Progresso", "Concluido"]
    ui_columns = st.columns(len(DEFAULT_COLUMN_NAMES), gap="medium", border=True)
    for column, column_widget in zip(DEFAULT_COLUMN_NAMES, ui_columns):
        db_task_step = task_step.ensure_created(schemas.TaskStepCreate(name=column))
        column_title(column_widget, column)
        for issue in db_task_step.issues:
            add_card(column_widget, issue)
