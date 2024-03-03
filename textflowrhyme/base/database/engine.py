from sqlalchemy import create_engine

from textflowrhyme.settings import settings

engine = create_engine(url=str(settings.database_dsn), echo=True)
