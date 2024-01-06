import httpx

from textflowrhyme.base.entities import Entity
from textflowrhyme.base.processors import Processor


class TextRewriteParams(Entity):
    """Payload to rewrite a text."""

    togetherai_api_key: str


class TextRewriter(Processor[str]):
    """Run prompt on Together.ai’s LLM."""

    ENDPOINT = "https://api.together.xyz/inference"
    PROMPT = "[INST] Rewrite the following text:\n{text} [/INST]"

    def __init__(self, text: str, params: TextRewriteParams) -> None:
        self.text = text
        self.params = params

    def _run(self) -> str:
        response = httpx.post(
            self.ENDPOINT,
            json={
                "model": "togethercomputer/llama-2-70b-chat",
                "max_tokens": 1024,
                "prompt": self.PROMPT.format(text=self.text),
                "request_type": "language-model-inference",
                "temperature": 1,
                "top_p": 0.7,
                "top_k": 50,
                "repetition_penalty": 1,
                "stop": ["[/INST]", "</s>"],
                "negative_prompt": "",
                "repetitive_penalty": 1,
            },
            headers={
                "Authorization": f"Bearer {self.params.togetherai_api_key}",
            },
            timeout=10,
        )
        return response.json()["output"]["choices"][0]["text"].strip()
