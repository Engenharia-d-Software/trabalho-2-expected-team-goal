from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from model import Base

ModelClass = TypeVar("ModelClass", bound=Base)
CreateSchemaClass = TypeVar("CreateSchemaClass", bound=BaseModel)
UpdateSchemaClass = TypeVar("UpdateSchemaClass", bound=BaseModel)


class Crud(Generic[ModelClass, CreateSchemaClass, UpdateSchemaClass]):
        
    def __init__(self, model_class: type[ModelClass]):
        self.__model_class = model_class

    def create(self, db: Session, db_in: CreateSchemaClass) -> ModelClass:
        db_obj = self.__model_class(**db_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_in: UpdateSchemaClass, db_obj: ModelClass) -> ModelClass:
        for key, value in db_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.merge(db_obj)
        db.commit()
        return db_obj

    def delete(self, db:Session, ident: int) -> ModelClass | None:
        db_obj = db.get(self.__model_class, ident)
        if db_obj:
            db.delete(db_obj)
            db.commit()
        return db_obj

    def get(self, db: Session, ident: int) -> ModelClass | None:
        return db.get(self.__model_class, ident)
