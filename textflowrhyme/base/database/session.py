from sqlalchemy.orm import sessionmaker

from textflowrhyme.base.database.engine import engine

Session = sessionmaker(engine, expire_on_commit=False)
