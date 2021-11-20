from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch
from GraphAlgorithms.Graph.graph import AdjacencyDict, Vertex

def main():
  G = AdjacencyDict(directed=True)
  # G.add_edge(Vertex('y'), Vertex('x'))
  # G.add_edge(Vertex('x'), Vertex('z'))
  # G.add_edge(Vertex('z'), Vertex('y'))
  # G.add_edge(Vertex('z'), Vertex('w'))
  # G.add_edge(Vertex('w'), Vertex('x'))
  # G.add_edge(Vertex('s'), Vertex('z'))
  # G.add_edge(Vertex('s'), Vertex('w'))
  # G.add_edge(Vertex('v'), Vertex('w'))
  # G.add_edge(Vertex('v'), Vertex('s'))
  # G.add_edge(Vertex('t'), Vertex('v'))
  # G.add_edge(Vertex('t'), Vertex('u'))
  # G.add_edge(Vertex('u'), Vertex('v'))
  # G.add_edge(Vertex('u'), Vertex('t'))

  G = AdjacencyDict(directed=True)
  G.add_edge(Vertex('s'), Vertex('z'))
  G.add_edge(Vertex('y'), Vertex('x'))
  G.add_edge(Vertex('x'), Vertex('z'))
  G.add_edge(Vertex('z'), Vertex('y'))
  G.add_edge(Vertex('z'), Vertex('w'))
  G.add_edge(Vertex('w'), Vertex('x'))
  G.add_edge(Vertex('s'), Vertex('w'))
  G.add_edge(Vertex('t'), Vertex('v'))
  G.add_edge(Vertex('v'), Vertex('w'))
  G.add_edge(Vertex('v'), Vertex('s'))  
  G.add_edge(Vertex('t'), Vertex('u'))
  G.add_edge(Vertex('u'), Vertex('v'))
  G.add_edge(Vertex('u'), Vertex('t'))
  # print(G.get_weight(Vertex('u'), Vertex('t')))
  dfs = DepthFirstSearch()
  dfs.traverse(G)
  print(dfs.dfs_t)
  return 0

if __name__=='__main__':
  main()