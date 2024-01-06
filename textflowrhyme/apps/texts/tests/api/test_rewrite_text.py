import pytest
from httpx import AsyncClient
from starlette import status


@pytest.mark.usefixtures("_mocked_inference_response")
async def test_rewrite_text(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/texts/rewrite",
        json={
            "text": "A sentence to rewrite.",
            "params": {
                "togetherai_api_key": "123",
            },
        },
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json == {
        "text": "Rewritten sentence.",
    }
