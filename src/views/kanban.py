import uuid
import streamlit as st
import streamlit_shadcn_ui as ui

import model

st.set_page_config(layout="wide")

def column_title(column, title):
    with column:
        st.header(title)

def add_card(column, issue: model.Issue):
    with column:
        card_key = str(uuid.uuid4())
        st.markdown(f"""
        <div key="{card_key}" style="
            background-color: #bfdbfe;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 0.5rem;
            border: 1px solid #d1d5db;
        ">
            <h3 style="
                color: #1e293b;
                font-weight: 600;
                font-size: 1.125rem;
                margin-bottom: 0.25rem;
            ">{issue.title}</h3>
            <p style="
                color: #475569;
                font-size: 0.875rem;
                margin: 0;
            ">{issue.description}</p>
        </div>
        """, unsafe_allow_html=True)

def render_kanban(columns: list[model.TaskStep]):
    ui_columns = st.columns(len(columns), gap="medium", border=True)
    for column, column_widget in zip(columns, ui_columns):
        column_title(column_widget, column.name)
        for db_issue in column.issues:
            add_card(column_widget, db_issue)
