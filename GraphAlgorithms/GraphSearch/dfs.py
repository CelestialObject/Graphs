from dataclasses import dataclass, field
from ..Graph.graph import AdjacencyDict, Vertex

@dataclass
class DepthFirstSearch:
  t : int = 0 # timer for discovery and finish
  k : int = 1 # number of connected components
  p : dict = field(default_factory=dict) # dfs predecessor tree parent
  d : dict = field(default_factory=dict) # discovery time during dfs [CLRS]
  f : dict = field(default_factory=dict) # finish exploring time of dfs [CLRS]
  cc : dict = field(default_factory=dict) # connected component of each vertex
  dfs_t : dict = field(default_factory=dict) # contains dfs_t of the edge (u,v)
  cycles : set() = field(default_factory=set)

  def set_dfs_edge_type(self, u : Vertex, v : Vertex, t : str) -> None:
    if (u not in self.dfs_t): self.dfs_t.setdefault(u, dict())
    if (v not in self.dfs_t[u]): self.dfs_t[u].update({v : t})
    return None
  
  def traverse(self, G : AdjacencyDict) -> None:
    self.t = 0
    self.k = 1
    for v in G.adj.keys():
      if (v not in self.p):
        self.p[v] = None
        self.cc[v] = self.k
        self.k += 1
        self.dfs_visit(G, v, self.t)
    return None
  
  def dfs_visit(self, G : AdjacencyDict, u : Vertex, t : int) -> None:
    self.t += 1
    self.d[u] = self.t
    for v in G.adj[u]:
      if (v not in self.p):
        # set u as parent of v
        self.p[v] = u
        # Set (u,v) as Tree edge, if G undirected, set (v,u) as tree edge
        self.set_dfs_edge_type(u, v, 't')
        if (not G.directed): self.set_dfs_edge_type(v, u, 't')
        # assign v to current connected component of u
        self.cc[v] = self.cc[u]
        # recurse in depth of v
        self.dfs_visit(G, v, t)
      elif (v not in self.f): # if did not finish v
        # set (u, v) back edge, if G undirected set (v, u) back edge
        self.set_dfs_edge_type(u, v, 'b')
        self.cycles.add(v) # since a back edge exists, G consist a cycle w/ v
        if (not G.directed): self.set_dfs_edge_type(v, u, 'b')
      else:
        if (G.directed): # if G undirected->forward and cross edge not possible
          if self.d[v] > self.d[u]: self.set_dfs_edge_type(u, v, 'f')
          else: self.set_dfs_edge_type(u, v, 'c')
    self.t += 1
    self.f[u] = self.t
    return None

  def is_dag(self, G : AdjacencyDict) -> bool:
    self.traverse(G)
    return ((G.directed) and (len(self.cycles) == 0))
  
  def topological_sort(self, G : AdjacencyDict) -> iter:
    if self.is_dag(G):
      # return iter(sorted(self.f.keys(), key=self.f.get, reverse=True))
      return iter(reversed(list(self.f.keys())))
    print("Given Graph is not a DAG, No topological sort possible")
    return iter([])
  
  def has_cycle(self, G : AdjacencyDict) -> iter:
    self.traverse(G)
    if (len(self.cycles) != 0):
      return iter(self.cycles)
    print(f'G has no cycles')
    return iter(set())
    