import string

import nltk

from textflowrhyme.apps.documents.entities.node import NodeDocument, NodeParagraph
from textflowrhyme.apps.trees.entities.tree import (
    Tree,
    TreeContext,
    TreeParagraph,
    TreeParagraphs,
    TreeSentence,
    TreeSentences,
    TreeSpan,
    TreeSpans,
    TreeSpanSubcategory,
)
from textflowrhyme.base.processors import Processor


class DocumentTreeConverter(Processor):
    """Create a tree from a document."""

    def __init__(self, document: NodeDocument) -> None:
        self.document = document
        self.context = TreeContext()

    def _run(self) -> Tree:
        tree = Tree(document=self.document, paragraphs=TreeParagraphs(), context=self.context)
        self.extract_paragraphs(tree)

        for paragraph in tree.paragraphs.collection:
            self.extract_sentences(paragraph)
            self.context.paragraph_count += 1

            sentences = filter(
                lambda item: isinstance(item, TreeSentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                self.extract_spans(sentence)
                self.context.sentence_count += 1

                self.context.word_count += sentence.spans.count
                self.context.sentence_lengths.append(sentence.spans.count)

        return tree

    def extract_paragraphs(self, tree: Tree) -> None:
        paragraphs_extractor = _TreeParagraphsExtractor(tree, self.context)
        paragraphs_extractor.run()

    def extract_sentences(self, paragraph: TreeParagraph) -> None:
        sentences_extractor = _TreeSentencesExtractor(paragraph, self.context)
        sentences_extractor.run()

    def extract_spans(self, sentence: TreeSentence) -> None:
        spans_extractor = _TreeSpansExtractor(sentence, self.context)
        spans_extractor.run()


class _TreeParagraphsExtractor(Processor):
    """Extract paragraphs from tree by concatenating its text nodes."""

    def __init__(self, tree: Tree, context: TreeContext | None = None) -> None:
        self.tree = tree
        self.context = context

    def _run(self) -> None:
        self.extract_paragraphs()

    def extract_paragraphs(self) -> None:
        self.tree.paragraphs.collection = [
            self.create_paragraph(node_paragraph) for node_paragraph in self.tree.document.content
        ]
        self.tree.paragraphs.count = len(self.tree.paragraphs.collection)

    def create_paragraph(self, node_paragraph: NodeParagraph) -> TreeParagraph:
        paragraph_content = ""
        for text_node in node_paragraph.content:
            paragraph_content += text_node.text

        return TreeParagraph(
            content=paragraph_content,
            sentences=TreeSentences(),
        )


class _TreeSentencesExtractor(Processor):
    """Extract a sentence collection from a given paragraph’s content."""

    def __init__(self, paragraph: TreeParagraph, context: TreeContext | None = None) -> None:
        self.paragraph = paragraph
        self.context = context
        self.sentence_count = 0

    def _run(self) -> dict:
        sentences = nltk.tokenize.PunktSentenceTokenizer().span_tokenize(self.paragraph.content)

        self.paragraph.sentences.collection = []
        previous_end_index = 0
        for start_index, end_index in sentences:
            if start_index != previous_end_index:
                whitespace = self.paragraph.content[previous_end_index:start_index]
                self.create_whitespace_span(content=whitespace)

            sentence = self.paragraph.content[start_index:end_index]
            self.create_sentence(content=sentence)
            self.sentence_count += 1

            previous_end_index = end_index

        maybe_end_index = len(self.paragraph.content)
        if previous_end_index < maybe_end_index:
            whitespace = self.paragraph.content[previous_end_index:maybe_end_index]
            self.create_whitespace_span(content=whitespace)

        self.paragraph.sentences.count = self.sentence_count

    def create_whitespace_span(self, content: str) -> TreeSpan:
        token = TreeSpan(
            content=content,
            subcategory=TreeSpanSubcategory.WHITESPACE,
        )
        self.paragraph.sentences.collection.append(token)

    def create_sentence(self, content: str) -> TreeSentence:
        sentence = TreeSentence(
            content=content,
            spans=TreeSpans(),
        )
        self.paragraph.sentences.collection.append(sentence)


class _TreeSpansExtractor(Processor):
    """Extract a span collection from a given sentence’s content."""

    # Mostly pointless due to SpanTokenizer’s internals
    PUNCTUATION = string.punctuation + "„“”‚‘’-–—"

    def __init__(self, sentence: TreeSentence, context: TreeContext | None = None) -> None:
        self.sentence = sentence
        self.context = context
        self.word_count = 0

    def _run(self) -> None:
        words = nltk.tokenize.TreebankWordTokenizer().span_tokenize(self.sentence.content)

        self.sentence.spans.collection = []
        previous_end_index = 0
        for start_index, end_index in words:
            if start_index != previous_end_index:
                self.create_span(
                    content=self.sentence.content[previous_end_index:start_index],
                    subcategory=TreeSpanSubcategory.WHITESPACE,
                )

            content = self.sentence.content[start_index:end_index]
            if content in self.PUNCTUATION:
                subcategory = TreeSpanSubcategory.PUNCTUATION
            else:
                subcategory = TreeSpanSubcategory.WORD
            self.create_span(
                content=content,
                subcategory=subcategory,
            )
            self.word_count += 1

            previous_end_index = end_index

        maybe_end_index = len(self.sentence.content)
        if previous_end_index < maybe_end_index:
            self.create_span(
                content=self.sentence.content[previous_end_index:maybe_end_index],
                subcategory=TreeSpanSubcategory.WHITESPACE,
            )

        self.sentence.spans.count = self.word_count

    def create_span(self, content: str, subcategory: str) -> None:
        span = TreeSpan(
            content=content,
            subcategory=subcategory,
        )
        self.sentence.spans.collection.append(span)
