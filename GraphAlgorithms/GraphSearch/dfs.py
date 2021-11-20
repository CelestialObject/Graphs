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

  def traverse(self, G : AdjacencyDict) -> None:
    self.t = 0
    self.k = 1
    for v in G.adj.keys():
      if (v not in self.p):
        self.p[v] = None
        self.cc[v] = self.k
        self.k += 1
        self.dfs_visit(G, v, self.t)
        print(self.cc)
    return None
  
  def dfs_visit(self, G : AdjacencyDict, u : Vertex, t : int) -> None:
    self.t += 1
    self.d[u] = self.t
    self.dfs_t.setdefault(u, dict())
    for v in G.adj[u]:
      if (v not in self.p):
        self.dfs_t[u].update({v : 't'}) # (u, v) tree edge
        self.cc[v] = self.cc[u]
        self.p[v] = u
        self.dfs_visit(G, v, t)
      elif (v not in self.f):
        self.dfs_t[u].update({v : 'b'}) # (u, v) back edge
      else:
        if self.d[v] > self.d[u]: self.dfs_t[u].update({v : 'f'})
        else: self.dfs_t[u].update({v : 'c'})
    self.t += 1
    self.f[u] = self.t
    return None
