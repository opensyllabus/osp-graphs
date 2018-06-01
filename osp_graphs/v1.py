

import networkx as nx

from sqlalchemy.dialects.postgresql import array_agg
from tqdm import tqdm
from itertools import combinations
from collections import Counter

from .v1_db import session, Text, Citation


class Graph(nx.Graph):

    @classmethod
    def from_text_ids(cls, text_ids):
        """Build graph from set of text ids.
        """
        graph = cls()

        doc_texts = (session
            .query(array_agg(Citation.text_id))
            .join(Text, Citation.text_id==Text.id)
            .filter(Text.valid==True)
            .filter(Text.display==True)
            .filter(Text.id.in_(text_ids))
            .group_by(Citation.document_id))

        edges = Counter()
        for ids in tqdm(doc_texts):
            for tid1, tid2 in combinations(ids[0], 2):
                edges[tid1, tid2] += 1

        for (tid1, tid2), count in edges.items():
            graph.add_edge(tid1, tid2, weight=count)

        texts = session.query(Text).filter(Text.id.in_(text_ids))

        for text in tqdm(texts):
            graph.add_node(text.id, title=text.title)

        return graph
