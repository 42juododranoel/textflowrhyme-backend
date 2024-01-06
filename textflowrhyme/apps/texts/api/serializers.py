from textflowrhyme.apps.texts.processors.text_rewriter import TextRewriteParams
from textflowrhyme.base.api.serializers import RequestSerializer, ResponseSerializer


class RewriteTextRequest(RequestSerializer):
    """Payload to rewrite text."""

    text: str
    params: TextRewriteParams


class RewriteTextResponse(ResponseSerializer):
    """Text rewriting response."""

    text: str
