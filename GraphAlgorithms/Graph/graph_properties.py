from ..Graph.graph import AdjacencyDict
from ..GraphSearch.dfs import DepthFirstSearch

def contains_cycle(G : AdjacencyDict) -> bool:
  dfs = DepthFirstSearch()
  dfs.traverse(G)
  for adj in dfs.dfs_t.values():
    if 'b' in adj.values(): return True # if a back edge exists after dfs
  return False
  
def is_dag(G : AdjacencyDict) -> bool:
  return ((G.directed) and (not contains_cycle(G)))
