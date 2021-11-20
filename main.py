from GraphAlgorithms.GraphSearch.bfs import BreadthFirstSearch
from GraphAlgorithms.Graph.graph import AdjacencyDict, Vertex

def main():
  G = AdjacencyDict(directed=False)
  G.add_edge(Vertex('a'), Vertex('z'))
  G.add_edge(Vertex('a'), Vertex('s'))
  G.add_edge(Vertex('s'), Vertex('x'))
  G.add_edge(Vertex('x'), Vertex('d'))
  G.add_edge(Vertex('x'), Vertex('c'))
  G.add_edge(Vertex('d'), Vertex('c'))
  G.add_edge(Vertex('d'), Vertex('f'))
  G.add_edge(Vertex('c'), Vertex('f'))
  G.add_edge(Vertex('c'), Vertex('v'))
  G.add_edge(Vertex('f'), Vertex('v'))
  # print(G)
  bfs = BreadthFirstSearch(s=Vertex('v'))
  bfs.traverse_graph(G)
  # print(set(G.get_out_neighbor(Vertex('c'))))
  # print(set(G.get_in_neighbor(Vertex('c'))))
  # print(bfs.get_levelset(4))
  # print(bfs.s, bfs.d[Vertex('a')])
  # print(bfs.get_shortest_path(Vertex('z')))
  # print(G.get_weight(Vertex('a'), Vertex('z')))
  return 0

if __name__=='__main__':
  main()