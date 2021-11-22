from ..Graph.graph import AdjacencyDict, Vertex
from dataclasses import dataclass, field

@dataclass
class ShortestPath:
  p : dict = field(default_factory=dict) # parent tree for shortest path
  d : dict = field(default_factory=dict) # shortest distance from vertex s

  def init_shortest_paths(self,
                          G : AdjacencyDict,
                          s : Vertex,
                          init_d : float = float('inf')) -> None:
    self.d.setdefault(s, dict())
    for v in G.adj: self.d[s][v] = init_d
    return None
  
  # def set_d(self, u : Vertex, v : Vertex, d : float = float('inf')) -> None:
  #   if u not in self.d:
  #     if v not in self.d[u]:
  #       self.d[u][v] = d
  #   return None
  
  # def get_d(self, u : Vertex, v : Vertex) -> float:
  #   if u in self.d:
  #     if v in self.d[u]:
  #       return self.d[u][v]
  #   return 

  def set_parent_tree(self, G : AdjacencyDict, s : Vertex) -> None:
    # assumes self.d is not empty
    if (not self.d[s]):
      # TODO : replace w/ best single source shortest path
      print("shortest paths haven't been computed")
      return None
    
    if (s not in G.adj):
      print(f'Source vertex : {self.s} is not in graph')
      return None

    self.p[s] = None
    for u in G.adj:
      if (self.d[s][u] not in [float('inf'), float('-inf')]): # d[s,u] is finite
        for v in G.adj[u]:
          if ((v not in self.p) and (self.d[s][v] == self.d[s][u] + G.get_weight(u,v))):
            self.p[v] = u
    return None
  
  def get_shortest_path(self, s : Vertex, v : Vertex) -> iter:
    sp = []
    if (s == v): sp.append(s)
    elif (v not in self.p):
      print(f'No path exists from {s} to {v}')
      return iter([])
    else:
      sp.extend(self.get_shortest_path(s, self.p[v]))
      sp.append(v)
    return iter(sp)

  def __repr__(self) -> str:
    reps = [f'{u} : {[(v, d) for v, d in dist.items()]}\n' for u, dist in self.d.items()]
    rep = ''
    for r in reps: rep += r
    return rep

