from math import floor
from typing import ClassVar

from textflowrhyme.apps.trees.entities.tree import (
    Tree,
    TreeSentence,
    TreeSpanSubcategory,
)
from textflowrhyme.base.entities import Entity
from textflowrhyme.base.processors import Processor


class AnalyzeFatigueParams(Entity):
    """Params sent from client to tweak analysis."""

    fatigue_rate: int


class TreeFatigueAnalyzer(Processor):
    """Analyze a tree fatigue."""

    PUNCTUATION_STRENGTH: ClassVar = {
        ",": 10,
        "—": 20,
        ";": 40,
    }

    def __init__(self, tree: Tree, params: AnalyzeFatigueParams) -> None:
        self.tree = tree
        self.params = params

    def _run(self) -> None:
        for paragraph in self.tree.paragraphs.collection:
            sentences = filter(
                lambda item: isinstance(item, TreeSentence),
                paragraph.sentences.collection,
            )
            previous_accumulated_fatigue = 0
            for sentence in sentences:
                previous_accumulated_fatigue = self.analyze_span_fatigue(
                    sentence,
                    floor(previous_accumulated_fatigue * 0.5),
                )

    def analyze_span_fatigue(self, sentence: TreeSentence, accumulated_fatigue: int) -> int:
        previous_word_fatigue = accumulated_fatigue

        for span in sentence.spans.collection:
            if span.subcategory == TreeSpanSubcategory.WHITESPACE:
                # Whitespace has same fatigue as previous span
                span.fatigue = floor(previous_word_fatigue)
            else:
                # Word or punctuation increment fatigue
                span.fatigue = floor(accumulated_fatigue)
                previous_word_fatigue = accumulated_fatigue
                accumulated_fatigue += 1

                if span.subcategory == TreeSpanSubcategory.PUNCTUATION:
                    # Try to reduce fatigue if punctuation
                    punctuation_strength = self.PUNCTUATION_STRENGTH.get(span.content, 0)
                    reduced_accumulated_fatigue = accumulated_fatigue - punctuation_strength
                    accumulated_fatigue = max(0, reduced_accumulated_fatigue)
                    previous_word_fatigue = accumulated_fatigue

        return accumulated_fatigue
