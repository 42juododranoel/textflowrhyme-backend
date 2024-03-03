from sqlalchemy import select
from sqlalchemy.orm import selectinload

from textflowrhyme.base.api.serializers import (
    CollectionResult,
    InstanceResult,
    InstanceTypeResult,
    Payload,
    Result,
)
from textflowrhyme.base.database.model import Model
from textflowrhyme.base.database.session import Session


class ViewShortcuts:
    """Use these shortcuts for common view tasks."""

    @classmethod
    def render_instance(
        cls,
        instance: Model,
        result_type: type[Result],
    ) -> InstanceResult[InstanceTypeResult]:
        return InstanceResult(
            instance=result_type(**instance.as_dict()),
        )

    @classmethod
    def render_collection(
        cls,
        collection: list[Model],
        result_type: type[Result],
    ) -> CollectionResult[InstanceTypeResult]:
        return CollectionResult(
            collection=[result_type(**instance.as_dict()) for instance in collection],
            count=len(collection),
        )

    @classmethod
    def list_collection(
        cls,
        model_type: type[Model],
        result_type: type[Result],
    ) -> CollectionResult[InstanceTypeResult]:
        with Session() as session:
            statement = select(model_type)
            if model_type.SELECTINS:
                statement = statement.options(selectinload(*model_type.SELECTINS))
            collection = session.scalars(statement).fetchall()

        return cls.render_collection(collection, result_type)

    @classmethod
    def retrieve_instance(
        cls,
        model_type: type[Model],
        instance_id: Model.Id,
        result_type: type[Result],
    ) -> InstanceResult[InstanceTypeResult]:
        with Session() as session:
            statement = select(model_type).where(model_type.id == instance_id)
            if model_type.SELECTINS:
                statement = statement.options(selectinload(*model_type.SELECTINS))
            instance = session.scalars(statement).unique().one()

        return cls.render_instance(instance, result_type)

    @classmethod
    def create_instance(
        cls,
        model_type: type[Model],
        payload: Payload,
        result_type: type[Result],
    ) -> InstanceResult[InstanceTypeResult]:
        with Session() as session:
            values = payload.dict(exclude_unset=True)
            instance = model_type(**values)
            session.add(instance)
            session.commit()

        return cls.retrieve_instance(model_type, instance.id, result_type)

    @classmethod
    def update_instance(
        cls,
        model_type: type[Model],
        instance_id: Model.Id,
        payload: Payload,
        result_type: type[Result],
    ) -> InstanceResult[InstanceTypeResult]:
        with Session() as session:
            values = payload.dict(exclude_unset=True)
            session.query(model_type).filter(model_type.id == instance_id).update(values)
            session.commit()

        return cls.retrieve_instance(model_type, instance_id, result_type)

    @classmethod
    def delete_instance(cls, model_type: type[Model], instance_id: Model.Id) -> None:
        with Session() as session:
            session.query(model_type).filter(model_type.id == instance_id).delete()
            session.commit()


view = ViewShortcuts()
