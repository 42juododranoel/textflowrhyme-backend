import pytest
from pytest_httpx._httpx_mock import HTTPXMock


@pytest.fixture
def _mocked_inference_response(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://api.together.xyz/inference",
        method="POST",
        json={
            "id": "83e304487ae87d29-EVN",
            "status": "finished",
            "prompt": ["[INST] Rewrite the following paragraph:\ntest text 123 [/INST]"],
            "model": "togethercomputer/llama-2-70b-chat",
            "model_owner": "",
            "num_returns": 1,
            "args": {
                "model": "togethercomputer/llama-2-70b-chat",
                "max_tokens": 1024,
                "prompt": "[INST] Rewrite the following paragraph:\ntest text 123 [/INST]",
                "request_type": "language-model-inference",
                "temperature": 1,
                "top_p": 0.7,
                "top_k": 50,
                "repetition_penalty": 1,
                "stop": ["[/INST]", "</s>"],
                "negative_prompt": "",
                "sessionKey": "5e307ba8-2ed8-4d93-9e80-5ee295fdba52",
                "repetitive_penalty": 1,
                "update_at": "2023-12-30T17:40:02.186Z",
            },
            "subjobs": [],
            "output": {
                "usage": {
                    "prompt_tokens": 20,
                    "completion_tokens": 89,
                    "total_tokens": 109,
                },
                "result_type": "language-model-inference",
                "choices": [
                    {
                        "text": "Rewritten sentence.",
                    },
                ],
            },
        },
    )
