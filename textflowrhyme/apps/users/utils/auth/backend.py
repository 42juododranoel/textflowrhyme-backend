from fastapi_users.authentication import AuthenticationBackend

from textflowrhyme.apps.users.utils.auth.strategy import get_jwt_strategy
from textflowrhyme.apps.users.utils.auth.transport import bearer_transport

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
