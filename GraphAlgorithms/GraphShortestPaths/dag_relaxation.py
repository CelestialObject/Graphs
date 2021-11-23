from dataclasses import dataclass
from ..GraphSearch.dfs import DepthFirstSearch
from ..Graph.graph import AdjacencyDict, Vertex
from GraphAlgorithms.GraphShortestPaths.shortest_path import ShortestPath

@dataclass
class DAGRelaxation(ShortestPath):
  def dag_relax(self, G: AdjacencyDict, s: Vertex, u: Vertex, v: Vertex) -> None:
    # triangle inequality based relaxation between (s,v), (s,u), and (u,v)
    shortest_d_sv = self.d[s][v]
    possible_shorter_d_sv = self.d[s][u] + G.get_weight(u, v)
    if (shortest_d_sv > possible_shorter_d_sv):
      self.d[s][v] = possible_shorter_d_sv
    return None

  def compute_shortest_path(self, G : AdjacencyDict, s : Vertex) -> None:
    self.init_shortest_paths(G, s)
    self.d[s][s] = 0
    dfs = DepthFirstSearch()
    for u in dfs.topological_sort(G):
      for v in G.adj[u]:
        self.dag_relax(G, s, u, v)
    
    self.set_parent_tree(G, s)
    return None