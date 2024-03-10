from fastapi_users.authentication import JWTStrategy

from textflowrhyme.apps.users.constants import LIFETIME, SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=LIFETIME)


jwt_strategy = get_jwt_strategy()
