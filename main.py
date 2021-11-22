# from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch
from GraphAlgorithms.Graph.graph import AdjacencyDict, Vertex
from GraphAlgorithms.GraphSearch.dfs import DepthFirstSearch
from GraphAlgorithms.GraphShortestPaths.dag_relaxation import DAGRelaxation

def main():
  G = AdjacencyDict(directed=True)
  G.add_edge(Vertex('a'), Vertex('b'), w=-5)
  G.add_edge(Vertex('b'), Vertex('f'), w=-4)
  G.add_edge(Vertex('b'), Vertex('e'), w=6)
  G.add_edge(Vertex('a'), Vertex('e'), w=7)
  G.add_edge(Vertex('e'), Vertex('f'), w=3)
  G.add_edge(Vertex('f'), Vertex('c'), w=8)
  G.add_edge(Vertex('f'), Vertex('g'), w=2)
  G.add_edge(Vertex('b'), Vertex('c'), w=-1)
  G.add_edge(Vertex('g'), Vertex('c'), w=1)
  G.add_edge(Vertex('g'), Vertex('h'), w=-2)
  G.add_edge(Vertex('h'), Vertex('d'), w=4)
  G.add_edge(Vertex('h'), Vertex('c'), w=9)
  G.add_edge(Vertex('d'), Vertex('c'), w=5)
  print(G)
  dagr = DAGRelaxation()
  dagr.compute_shortest_path(G, Vertex('e'))
  print(dagr, dagr.p, list(dagr.get_shortest_path(Vertex('e'), Vertex('c'))))
  # dfs = DepthFirstSearch()
  # dfs.traverse(G)
  # print(dfs.d, dfs.f, dfs.cc)
  # print(dfs.dfs_t)
  # print(list(dfs.topological_sort(G)), list(dfs.has_cycle(G)))
  # print(list(dfs.has_cycle(G)))
  # ts = dfs.topological_sort(G)
  # print(list(ts))

  return 0

if __name__=='__main__':
  main()