from sqlalchemy import select
from sqlalchemy.orm import selectinload

from textflowrhyme.base.api.serializers import (
    CollectionResponseSerializer,
    InstanceResponseSerializer,
    InstanceSerializerType,
    Serializer,
)
from textflowrhyme.base.database.model import BaseModel
from textflowrhyme.base.database.session import Session


class ViewShortcuts:
    """Use these shortcuts for common view tasks."""

    @classmethod
    def render_instance(
        cls,
        instance: BaseModel,
        serializer: Serializer,
    ) -> InstanceResponseSerializer[InstanceSerializerType]:
        return InstanceResponseSerializer(
            instance=serializer(**instance.as_dict()),
        )

    @classmethod
    def render_collection(
        cls,
        collection: list[BaseModel],
        list_serializer: Serializer,
    ) -> CollectionResponseSerializer[InstanceSerializerType]:
        return CollectionResponseSerializer(
            collection=[list_serializer(**instance.as_dict()) for instance in collection],
            count=len(collection),
        )

    @classmethod
    def list_collection(
        cls,
        model: BaseModel,
        list_serializer: Serializer,
    ) -> CollectionResponseSerializer[InstanceSerializerType]:
        with Session() as session:
            statement = select(model).options(selectinload(*model.SELECTINS))
            collection = session.scalars(statement).fetchall()

        return cls.render_collection(collection, list_serializer)

    @classmethod
    def retrieve_instance(
        cls,
        model: BaseModel,
        instance_id: BaseModel.Id,
        retrieve_serializer: Serializer,
    ) -> InstanceResponseSerializer[InstanceSerializerType]:
        with Session() as session:
            statement = (
                select(model).where(model.id == instance_id).options(selectinload(*model.SELECTINS))
            )
            instance = session.scalars(statement).unique().one()

        return cls.render_instance(instance, retrieve_serializer)

    @classmethod
    def create_instance(
        cls,
        model: BaseModel,
        payload: Serializer,
        retrieve_serializer: Serializer,
    ) -> InstanceResponseSerializer[InstanceSerializerType]:
        with Session() as session:
            instance = model(**payload.dict())
            session.add(instance)
            session.commit()

        return cls.retrieve_instance(model, instance.id, retrieve_serializer)

    @classmethod
    def update_instance(
        cls,
        model: BaseModel,
        instance_id: BaseModel.Id,
        payload: Serializer,
        retrieve_serializer: Serializer,
    ) -> InstanceResponseSerializer[InstanceSerializerType]:
        with Session() as session:
            session.query(model).filter(model.id == instance_id).update(payload.dict())
            session.commit()

        return cls.retrieve_instance(model, instance_id, retrieve_serializer)

    @classmethod
    def delete_instance(cls, model: BaseModel, instance_id: BaseModel.Id) -> None:
        with Session() as session:
            session.query(model).filter(model.id == instance_id).delete()
            session.commit()


view = ViewShortcuts()
