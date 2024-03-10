from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from textflowrhyme.apps.users.models.user import User
from textflowrhyme.base.database.session import get_asession


async def get_user_database(asession: AsyncSession = Depends(get_asession)):
    yield SQLAlchemyUserDatabase(asession, User)
