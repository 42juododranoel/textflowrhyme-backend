# from collections.abc import AsyncGenerator

# import pytest
# from fastapi import FastAPI
# from httpx import AsyncClient

# from textflowrhyme.app import get_app
# from textflowrhyme.base.database.engine import engine
# from textflowrhyme.base.database.model import BaseModel

# NOT_PROVIDED = object()


# @pytest.fixture
# def app() -> FastAPI:
#     """FastAPI app."""
#     return get_app()


# @pytest.fixture(scope="session", autouse=True)
# def anyio_backend() -> str:
#     """Allow running async tests before each pytest run."""
#     return "asyncio"


# @pytest.fixture(autouse=True)
# async def recreate_tables(request) -> None:
#     """Recreate all tables before each test run."""

#     async with engine.begin() as connection:
#         await connection.run_sync(BaseModel.metadata.drop_all)
#         await connection.run_sync(BaseModel.metadata.create_all)


# @pytest.fixture
# async def as_anon(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
#     """Test client."""
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         yield client



##################################################################################################


# import contextlib
# import uuid
# from argparse import Namespace
# from pathlib import Path
# from typing import AsyncIterator, Optional, Union

# import sqlalchemy as sa
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy_utils.functions.database import (
#     _set_url_database,
#     _sqlite_file_exists,
#     make_url,
# )
# from sqlalchemy_utils.functions.orm import quote

# async def create_database_async(
#     url: str, 
#     encoding: str = "utf8", 
#     template: str | None = None,
# ) -> None:
#     url = make_url(url)
#     database = url.database
#     dialect_name = url.get_dialect().name
#     dialect_driver = url.get_dialect().driver

#     if dialect_name == "postgresql":
#         url = _set_url_database(url, database="postgres")
#     elif not dialect_name == "sqlite":
#         url = _set_url_database(url, database=None)

#     if dialect_name == "postgresql" and dialect_driver in {"asyncpg", "pg8000", "psycopg2", "psycopg2cffi"}:
#         engine = create_async_engine(url, isolation_level="AUTOCOMMIT")
#     else:
#         engine = create_async_engine(url)

#     if dialect_name == "postgresql":
#         if not template:
#             template = "template1"

#         async with engine.begin() as conn:
#             text = "CREATE DATABASE {} ENCODING '{}' TEMPLATE {}".format(
#                 quote(conn, database), 
#                 encoding, 
#                 quote(conn, template),
#             )
#             await conn.execute(sa.text(text))

#     elif dialect_name == "sqlite" and database != ":memory:":
#         if database:
#             async with engine.begin() as conn:
#                 await conn.execute(sa.text("CREATE TABLE DB(id int)"))
#                 await conn.execute(sa.text("DROP TABLE DB"))

#     else:
#         async with engine.begin() as conn:
#             text = f"CREATE DATABASE {quote(conn, database)}"
#             await conn.execute(sa.text(text))

#     await engine.dispose()


###################################################################################################

# import pytest
# import pytest_asyncio
# import sqlalchemy
# from sqlalchemy.ext.asyncio import (
#     AsyncSession,
#     # create_async_engine,
#     async_scoped_session,
#     AsyncConnection,
# )

# # async_engine = create_async_engine(
# #     cfg("DB_URL_ASYNC"), pool_size=10, echo=True, max_overflow=10
# # )

# # TestingAsyncSessionLocal = sessionmaker(
# #     async_engine,
# #     expire_on_commit=False,
# #     autoflush=False,
# #     autocommit=False,
# #     class_=AsyncSession,
# # )

# from textflowrhyme.base.database import get_session


# @pytest_asyncio.fixture(scope="function")
# async def async_db_session():   
#     connection = await engine.connect()
#     trans = await connection.begin()
#     # async_session = TestingAsyncSessionLocal(bind=connection)

#     async_session = get_session()
#     nested = await connection.begin_nested()

#     @event.listens_for(async_session.sync_session, "after_transaction_end")
#     def end_savepoint(session, transaction):
#         nonlocal nested

#         if not nested.is_active:
#             nested = connection.sync_connection.begin_nested()

#     yield async_session

#     await trans.rollback()
#     await async_session.close()
#     await connection.close()



# # @pytest.fixture
# # async def user():
# #     async with get_session_context() as session:
# #         async with get_user_database_context(session) as user_database:
# #             async with get_user_manager_context(user_database) as user_manager:
# #                 yield await user_manager.create(
# #                     UserCreateSerializer(
# #                         email="user@user.user",
# #                         password="password1234",
# #                     )
# #                 )
