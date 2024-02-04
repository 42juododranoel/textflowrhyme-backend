import pytest
from httpx import AsyncClient

pytestmark = [pytest.mark.anyio]


async def test_analyze_fatigue(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/documents/analyze",
        json={
            "params": {
                "pos": {
                    "stub": True,
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
                            "marks": [{"type": "pos", "attrs": {"value": "wp"}}],
                        },
                        {"type": "text", "text": " ", "marks": []},
                        {
                            "type": "text",
                            "text": "is",
                            "marks": [{"type": "pos", "attrs": {"value": "vbz"}}],
                        },
                        {"type": "text", "text": " ", "marks": []},
                        {
                            "type": "text",
                            "text": "it",
                            "marks": [{"type": "pos", "attrs": {"value": "prp"}}],
                        },
                        {"type": "text", "text": "?", "marks": []},
                    ],
                },
            ],
        },
    }
