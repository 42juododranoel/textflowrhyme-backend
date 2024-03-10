from fastapi import APIRouter

from textflowrhyme.apps.users.api.serializers.user import UserSerializer, UserUpdateSerializer
from textflowrhyme.apps.users.utils.fastapi_users import fastapi_users

router = APIRouter()
tag = "users"

router.include_router(
    fastapi_users.get_users_router(UserSerializer, UserUpdateSerializer),
    tags=[tag],
)
