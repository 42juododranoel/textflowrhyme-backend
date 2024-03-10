from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status


async def test_auth_forgot_password(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/auth/forgot-password",
        json={
            "email": "user@example.com",
        },
    )

    response_json = response.json()
    assert response_json is None
    assert response.status_code == status.HTTP_202_ACCEPTED
