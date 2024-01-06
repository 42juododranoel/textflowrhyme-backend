from fastapi import APIRouter

from textflowrhyme.apps.documents.api.serializers import (
    DocumentAnalyzeRequest,
    DocumentAnalyzeResponse,
)
from textflowrhyme.apps.documents.processors.document_analyzer import DocumentAnalyzer

router = APIRouter()


@router.post("/analyze")
async def analyze(payload: DocumentAnalyzeRequest) -> DocumentAnalyzeResponse:
    """Analyze document fatigue."""

    document_analyzer = DocumentAnalyzer(
        document=payload.document,
        params=payload.params,
    )
    document = document_analyzer.run()

    return DocumentAnalyzeResponse(document=document)
