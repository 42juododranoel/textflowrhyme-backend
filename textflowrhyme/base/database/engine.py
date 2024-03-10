from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from textflowrhyme.settings import settings

engine_kwargs = {"echo": True,}

engine = create_engine(url=str(settings.database_dsn), **engine_kwargs,)
aengine = create_async_engine(url=str(settings.database_adsn), **engine_kwargs,)
