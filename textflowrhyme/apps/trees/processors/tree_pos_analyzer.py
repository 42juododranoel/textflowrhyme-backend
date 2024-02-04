import nltk

from textflowrhyme.apps.trees.entities.tree import (
    Tree,
    TreeSentence,
    TreeSpanSubcategory,
)
from textflowrhyme.base.entities import Entity
from textflowrhyme.base.processors import Processor


class AnalyzePosParams(Entity):
    """Params sent from client to tweak analysis."""

    stub: bool = True


class TreePosAnalyzer(Processor):
    """Analyze a tree PoS."""

    def __init__(self, tree: Tree, params: AnalyzePosParams) -> None:
        self.tree = tree
        self.params = params

    def _run(self) -> None:
        for paragraph in self.tree.paragraphs.collection:
            sentences = filter(
                lambda item: isinstance(item, TreeSentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                self.analyze_span_pos(sentence)

    def analyze_span_pos(self, sentence: TreeSentence) -> None:
        for span in sentence.spans.collection:
            if span.subcategory == TreeSpanSubcategory.WORD:
                span.pos = nltk.pos_tag([span.content])[0][1].lower()
