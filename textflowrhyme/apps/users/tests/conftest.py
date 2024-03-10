import contextlib
import pytest

from textflowrhyme.base.database.session import get_session, get_session_context
from textflowrhyme.apps.users.utils.database import get_user_database
from textflowrhyme.apps.users.utils.manager import get_user_manager
from textflowrhyme.apps.users.api.serializers.user import UserCreateSerializer

get_user_database_context = contextlib.asynccontextmanager(get_user_database)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


@pytest.fixture
async def user():
    async with get_session_context() as session:
        async with get_user_database_context(session) as user_database:
            async with get_user_manager_context(user_database) as user_manager:
                yield await user_manager.create(
                    UserCreateSerializer(
                        email="user@user.user",
                        password="password1234",
                    )
                )
