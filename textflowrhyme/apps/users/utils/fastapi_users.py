import uuid

from fastapi_users import FastAPIUsers

from textflowrhyme.apps.users.utils.auth.backend import auth_backend
from textflowrhyme.apps.users.utils.manager import get_user_manager
from textflowrhyme.apps.users.models.user import User

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
