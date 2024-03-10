from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status


async def test_auth_register(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/auth/register",
        json={
            "email": "user@example.com",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
        },
    )

    response_json = response.json()
    assert response_json == {
        'id': ANY, 
        'email': 'user@example.com', 
        'is_active': True, 
        'is_superuser': False, 
        'is_verified': False,
    }
    assert response.status_code == status.HTTP_201_CREATED
