from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password1234@localhost/textflowrhyme"

engine = create_engine(
    url=DATABASE_URL,
    echo=True,
)
