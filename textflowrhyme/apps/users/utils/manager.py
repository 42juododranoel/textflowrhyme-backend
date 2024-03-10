import uuid

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from textflowrhyme.apps.users.constants import SECRET
from textflowrhyme.apps.users.utils.database import get_user_database
from textflowrhyme.apps.users.models.user import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_database)):
    yield UserManager(user_db)
