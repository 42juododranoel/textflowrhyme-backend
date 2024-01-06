import pytest
from httpx import AsyncClient
from starlette import status

pytestmark = [pytest.mark.anyio]


async def test_analyze_length(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/documents/analyze",
        json={
            "params": {
                "length": {
                    "lengths": None,
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
                                "text": "Word. Two words. The Three Words.",
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
                            "text": "Word",
                            "marks": [{"type": "length", "attrs": {"value": 0}}],
                        },
                        {
                            "type": "text",
                            "text": ".",
                            "marks": [{"type": "length", "attrs": {"value": 0}}],
                        },
                        {"type": "text", "text": " ", "marks": []},
                        {
                            "type": "text",
                            "text": "Two",
                            "marks": [{"type": "length", "attrs": {"value": 1}}],
                        },
                        {
                            "type": "text",
                            "text": " ",
                            "marks": [{"type": "length", "attrs": {"value": 1}}],
                        },
                        {
                            "type": "text",
                            "text": "words",
                            "marks": [{"type": "length", "attrs": {"value": 1}}],
                        },
                        {
                            "type": "text",
                            "text": ".",
                            "marks": [{"type": "length", "attrs": {"value": 1}}],
                        },
                        {"type": "text", "text": " ", "marks": []},
                        {
                            "type": "text",
                            "text": "The",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                        {
                            "type": "text",
                            "text": " ",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                        {
                            "type": "text",
                            "text": "Three",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                        {
                            "type": "text",
                            "text": " ",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                        {
                            "type": "text",
                            "text": "Words",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                        {
                            "type": "text",
                            "text": ".",
                            "marks": [{"type": "length", "attrs": {"value": 2}}],
                        },
                    ],
                },
            ],
        },
    }
    assert response.status_code == status.HTTP_200_OK
