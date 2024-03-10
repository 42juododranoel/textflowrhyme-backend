from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from textflowrhyme.base.database.engine import engine, aengine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

sessionmaker_kwargs = {
    "expire_on_commit": False,
}

Asession = async_sessionmaker(aengine, **sessionmaker_kwargs)
Session = sessionmaker(engine, **sessionmaker_kwargs)


async def get_asession() -> AsyncGenerator[AsyncSession, None]:
    async with Asession() as asession:
        yield asession
