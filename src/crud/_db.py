from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

_engine = create_engine(
    "sqlite:///mydb.sqlite",
    connect_args={"check_same_thread": False}
)

_session_builder = sessionmaker(bind=_engine, autocommit=False, autoflush=False, class_=Session)

def get_session():
    return _session_builder()


def create_all(base_class: DeclarativeBase):
    base_class.metadata.create_all(bind=_engine)
