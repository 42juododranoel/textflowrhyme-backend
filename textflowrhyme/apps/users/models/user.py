from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from textflowrhyme.base.database.model import Model


class User(SQLAlchemyBaseUserTableUUID, Model):
    pass
