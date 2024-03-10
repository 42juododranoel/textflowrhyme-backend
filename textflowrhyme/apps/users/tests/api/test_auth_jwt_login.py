from unittest.mock import ANY
from callee import String

from httpx import AsyncClient
from starlette import status


async def test_auth_jwt_login(as_anon: AsyncClient, user):
    response = await as_anon.post(
        "/api/v1.0.0/auth/jwt/login",
        data={
            "username": "user@user.user",
            "password": "password1234",
        },
    )

    response_json = response.json()
    assert response_json == {
        'access_token': String(), 
        'token_type': 'bearer',
    }
    assert response.status_code == status.HTTP_200_OK
