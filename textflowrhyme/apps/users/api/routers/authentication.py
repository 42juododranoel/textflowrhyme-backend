from fastapi import APIRouter

from textflowrhyme.apps.users.utils.auth.backend import auth_backend
from textflowrhyme.apps.users.api.serializers.user import UserCreateSerializer, UserSerializer
from textflowrhyme.apps.users.utils.fastapi_users import fastapi_users

router = APIRouter()
tag = "authentication"

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=[tag],
)
router.include_router(
    fastapi_users.get_register_router(UserSerializer, UserCreateSerializer),
    tags=[tag],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=[tag],
)
router.include_router(
    fastapi_users.get_verify_router(UserSerializer),
    tags=[tag],
)
