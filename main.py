# from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch
from GraphAlgorithms.Graph.graph import AdjacencyDict, Vertex
from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch

def main():
  G = AdjacencyDict(directed=True)
  G.add_edge(Vertex('Shirt'), Vertex('tie'))
  G.add_edge(Vertex('tie'), Vertex('jacket'))
  G.add_edge(Vertex('Shirt'), Vertex('belt'))
  G.add_edge(Vertex('belt'), Vertex('jacket'))
  G.add_edge(Vertex('pants'), Vertex('belt'))
  G.add_edge(Vertex('undershorts'), Vertex('pants'))
  G.add_edge(Vertex('undershorts'), Vertex('shoes'))
  G.add_edge(Vertex('pants'), Vertex('shoes'))
  G.add_edge(Vertex('socks'), Vertex('shoes'))
  G.add_vertex(Vertex('watch'))
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