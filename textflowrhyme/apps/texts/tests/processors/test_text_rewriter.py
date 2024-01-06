import pytest

from textflowrhyme.apps.texts.processors.text_rewriter import (
    TextRewriteParams,
    TextRewriter,
)

pytestmark = [pytest.mark.anyio]


@pytest.mark.usefixtures("_mocked_inference_response")
def test_text_rewriter():
    text_rewriter = TextRewriter(
        text="A sentence to rewrite.",
        params=TextRewriteParams(togetherai_api_key="123"),
    )

    text = text_rewriter.run()

    assert text == "Rewritten sentence."
