from sqlalchemy import select

from textflowrhyme.base.database.engine import engine
from textflowrhyme.base.database.model import BaseModel
from textflowrhyme.base.database.session import Session


class DatabaseShortcuts:
    """Use this to perform common SQL tasks."""

    @classmethod
    def get(cls, model: type[BaseModel], instance_id: BaseModel.Id | None = None) -> BaseModel:
        statement = select(model)

        if instance_id:
            statement = statement.where(model.id == instance_id)

        with Session() as session:
            return session.scalars(statement).one()

    @classmethod
    def delete(cls, model: type[BaseModel], instance_id: BaseModel.Id) -> None:
        with Session() as session:
            session.query(model).filter(model.id == instance_id).delete()
            session.commit()

    @classmethod
    def refresh(cls, instance: BaseModel) -> None:
        with Session() as session:
            session.refresh(instance)

    @classmethod
    def recreate_tables(cls) -> None:
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)


database = DatabaseShortcuts()
