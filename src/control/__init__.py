import streamlit as st

import crud

if "db_session" not in st.session_state:
    st.session_state.db_session = crud.get_session()

_db_session = st.session_state.db_session
