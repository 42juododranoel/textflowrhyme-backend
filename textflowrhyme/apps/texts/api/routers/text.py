from fastapi import APIRouter

from textflowrhyme.apps.texts.api.serializers import (
    RewriteTextRequest,
    RewriteTextResponse,
)
from textflowrhyme.apps.texts.processors.text_rewriter import TextRewriter

router = APIRouter()


@router.post("/rewrite")
async def rewrite_text(payload: RewriteTextRequest) -> RewriteTextResponse:
    """Rewrite text with AI."""

    text_rewriter = TextRewriter(
        text=payload.text,
        params=payload.params,
    )
    text = text_rewriter.run()

    return RewriteTextResponse(text=text)
