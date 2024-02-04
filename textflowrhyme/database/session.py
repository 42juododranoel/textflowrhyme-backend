from sqlalchemy.orm import sessionmaker

from textflowrhyme.database.engine import engine

Session = sessionmaker(engine, expire_on_commit=False)
