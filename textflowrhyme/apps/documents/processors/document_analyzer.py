from textflowrhyme.apps.documents.entities.node import NodeDocument
from textflowrhyme.apps.documents.processors.document_tree_converter import (
    DocumentTreeConverter,
)
from textflowrhyme.apps.trees.processors.tree_document_converter import (
    TreeDocumentConverter,
)
from textflowrhyme.apps.trees.processors.tree_fatigue_analyzer import (
    AnalyzeFatigueParams,
    TreeFatigueAnalyzer,
)
from textflowrhyme.apps.trees.processors.tree_length_analyzer import (
    AnalyzeLengthParams,
    TreeLengthAnalyzer,
)
from textflowrhyme.base.entities import Entity
from textflowrhyme.base.processors import Processor


class DocumentAnalyzeParams(Entity):
    """Payload to analyze document."""

    fatigue: AnalyzeFatigueParams | None = None
    length: AnalyzeLengthParams | None = None


class DocumentAnalyzer(Processor[NodeDocument]):
    """Analyze a document fatigue."""

    def __init__(self, document: NodeDocument, params: DocumentAnalyzeParams) -> None:
        self.document = document
        self.params = params

    def _run(self) -> NodeDocument:
        # Document -> Tree
        document_tree_converter = DocumentTreeConverter(document=self.document)
        tree = document_tree_converter.run()

        # Optionally analyze fatigue
        if self.params.fatigue:
            tree_fatigue_analyzer = TreeFatigueAnalyzer(tree=tree, params=self.params.fatigue)
            tree_fatigue_analyzer.run()

        # Optionally analyze length
        if self.params.length:
            tree_length_analyzer = TreeLengthAnalyzer(tree=tree, params=self.params.length)
            tree_length_analyzer.run()

        # Tree -> Document
        tree_document_converter = TreeDocumentConverter(tree=tree)
        return tree_document_converter.run()
