# from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch
from GraphAlgorithms.Graph.graph import AdjacencyDict, Vertex
from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch

def main():
  G = AdjacencyDict(directed=True)
  G.add_edge(Vertex('s'), Vertex('z'))
  G.add_edge(Vertex('s'), Vertex('w'))
  G.add_edge(Vertex('z'), Vertex('y'))
  G.add_edge(Vertex('z'), Vertex('w'))
  G.add_edge(Vertex('y'), Vertex('x'))
  G.add_edge(Vertex('x'), Vertex('z'))
  G.add_edge(Vertex('w'), Vertex('x'))
  G.add_edge(Vertex('t'), Vertex('v'))
  G.add_edge(Vertex('v'), Vertex('s'))
  G.add_edge(Vertex('v'), Vertex('w'))
  G.add_edge(Vertex('t'), Vertex('u'))
  G.add_edge(Vertex('u'), Vertex('t'))
  G.add_edge(Vertex('u'), Vertex('v'))
  print(G)
  dfs = DepthFirstSearch()
  dfs.traverse(G)
  print(dfs.d, dfs.f, dfs.cc)
  print(dfs.dfs_t)
  print(list(dfs.topological_sort(G)), list(dfs.has_cycle(G)))
  # print(list(dfs.has_cycle(G)))
  # ts = dfs.topological_sort(G)
  # print(list(ts))

  return 0

if __name__=='__main__':
  main()