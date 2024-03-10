import uuid

from fastapi_users import schemas


class UserSerializer(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreateSerializer(schemas.BaseUserCreate):
    pass


class UserUpdateSerializer(schemas.BaseUserUpdate):
    pass
