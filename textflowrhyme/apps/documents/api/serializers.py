from textflowrhyme.apps.documents.entities.node import NodeDocument
from textflowrhyme.apps.documents.processors.document_analyzer import (
    DocumentAnalyzeParams,
)
from textflowrhyme.base.api.serializers import RequestSerializer, ResponseSerializer


class DocumentAnalyzeRequest(RequestSerializer):
    """Payload to analyze document fatigue."""

    params: DocumentAnalyzeParams
    document: NodeDocument


class DocumentAnalyzeResponse(ResponseSerializer):
    """Response to analyze document fatigue request."""

    document: NodeDocument
