import kmeans1d

from textflowrhyme.apps.trees.entities.tree import Tree, TreeSentence
from textflowrhyme.base.entities import Entity
from textflowrhyme.base.processors import Processor


class AnalyzeLengthParams(Entity):
    """Params sent from client to tweak analysis."""

    lengths: None = None


class TreeLengthAnalyzer(Processor):
    """Analyze a tree length."""

    def __init__(self, tree: Tree, params: AnalyzeLengthParams) -> None:
        self.tree = tree
        self.params = params

    def _run(self) -> None:
        if self.params.lengths is None:
            self.analyze_by_kmeans()

    def analyze_by_kmeans(self) -> None:
        lengths: dict[int, int] = {}

        # Split lengths into three clusters
        clusters, _ = kmeans1d.cluster(self.tree.context.sentence_lengths, 3)
        for sentence_index, centroid_index in enumerate(clusters):
            sentence_length = self.tree.context.sentence_lengths[sentence_index]
            lengths[sentence_length] = centroid_index

        # Set length for each sentence
        for paragraph in self.tree.paragraphs.collection:
            sentences = filter(
                lambda item: isinstance(item, TreeSentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                sentence.length = lengths[sentence.spans.count]
