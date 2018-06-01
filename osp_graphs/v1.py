

import networkx as nx

from sqlalchemy.dialects.postgresql import array_agg
from tqdm import tqdm
from itertools import combinations
from collections import Counter

from v1_db import session, Text, Citation


class Graph(nx.Graph):

    def add_osp_edges(self):
        """Register edges from `citation`.
        """
        doc_text_ids = (session
            .query(array_agg(Citation.text_id))
            .join(Text, Citation.text_id==Text.id)
            .filter(Text.valid==True)
            .filter(Text.display==True)
            .group_by(Citation.document_id)
            .limit(1000))

        edges = Counter()
        for ids in tqdm(doc_text_ids):
            for tid1, tid2 in combinations(ids[0], 2):
                edges[tid1, tid2] += 1

        for (tid1, tid2), count in edges.items():
            self.add_edge(tid1, tid2, weight=count)
