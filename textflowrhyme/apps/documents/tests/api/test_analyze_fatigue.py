import pytest
from httpx import AsyncClient
from starlette import status

pytestmark = [pytest.mark.anyio]


async def test_analyze_fatigue(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/documents/analyze",
        json={
            "params": {
                "fatigue": {
                    "fatigue_rate": 1,
                },
            },
            "document": {
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": "What is it?",
                            },
                        ],
                    },
                ],
            },
        },
    )

    response_json = response.json()
    assert response_json == {
        "document": {
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "What",
                            "marks": [
                                {"type": "fatigue", "attrs": {"value": 0}},
                            ],
                        },
                        {
                            "type": "text",
                            "text": " ",
                            "marks": [
                                {"type": "fatigue", "attrs": {"value": 0}},
                            ],
                        },
                        {
                            "type": "text",
                            "text": "is",
                            "marks": [
                                {"type": "fatigue", "attrs": {"value": 1}},
                            ],
                        },
                        {
                            "type": "text",
                            "text": " ",
                            "marks": [
                                {"type": "fatigue", "attrs": {"value": 1}},
                            ],
                        },
                        {
                            "type": "text",
                            "text": "it",
                            "marks": [
                                {"type": "fatigue", "attrs": {"value": 2}},
                            ],
                        },
                        {
                            "type": "text",
                            "text": "?",
                            "marks": [
                                {
                                    "type": "fatigue",
                                    "attrs": {"value": 3},  # This is technically wrong, but OK
                                },
                            ],
                        },
                    ],
                },
            ],
        },
    }
    assert response.status_code == status.HTTP_200_OK
