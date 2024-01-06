from textflowrhyme.apps.documents.entities.node import (
    NodeDocument,
    NodeMark,
    NodeMarkAttrs,
    NodeMarkType,
    NodeParagraph,
    NodeText,
)
from textflowrhyme.apps.trees.entities.tree import Tree, TreeSentence, TreeSpan
from textflowrhyme.base.processors import Processor


class TreeDocumentConverter(Processor):
    """Create a document from a tree."""

    def __init__(self, tree: Tree) -> None:
        self.tree = tree

    def _run(self) -> NodeDocument:
        document = NodeDocument()

        for paragraph in self.tree.paragraphs.collection:
            node_paragraph = NodeParagraph()

            for item in paragraph.sentences.collection:
                if isinstance(item, TreeSentence):
                    for span in item.spans.collection:
                        node_text = self.create_node_text(span, item)
                        node_paragraph.content.append(node_text)
                else:
                    node_text = NodeText(text=item.content)
                    node_paragraph.content.append(node_text)

            document.content.append(node_paragraph)

        return document

    def create_node_text(
        self,
        span: TreeSpan,
        sentence: TreeSentence,
    ) -> NodeText:
        marks = []

        if span.fatigue is not None:
            fatigue_mark = NodeMark(
                type=NodeMarkType.FATIGUE,
                attrs=NodeMarkAttrs(value=span.fatigue),
            )
            marks.append(fatigue_mark)

        if sentence.length is not None:
            length_mark = NodeMark(
                type=NodeMarkType.LENGTH,
                attrs=NodeMarkAttrs(value=sentence.length),
            )
            marks.append(length_mark)

        return NodeText(
            text=span.content,
            marks=marks,
        )
