# --version > python3.10 is must 
# My implementation of graphs and graph algorithms
from typing import Any
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class Vertex:
  item : Any

  def __str__(self) -> str:
    return str(self.item)
  
  def __repr__(self) -> str:
    return str(self.item)

@dataclass
class Graph:
  directed : bool = False

@dataclass(slots=True)
class AdjacencyDict(Graph):
  """
  Graph represented as a dictionary of dictionaries
  G = (V, E) = {
    u1 : { e1 : w1, e2 : w2, ... },
    u2 : { vertex connected to u2 : weight on the edge},
    ...
  }
  """
  adj : dict = field(default_factory=dict)

  def add_vertex(self, v : Vertex) -> None:
    """ 
    Adds vertex v as the key to the adjacency dictionary
    default value: empty dictionary. 
    if v already exists as a key, does nothing
    """
    self.adj.setdefault(v, dict())
    return None
  
  def remove_vertex(self, v : Vertex) -> None:
    """
    deletes the vertex v key from the adjacency dict
    removes the value v from all the keys u in the adjacency dict
    """
    if v in self.adj: del self.adj[v]
    for u in self.adj.keys():
      if v in self.adj[u]: del self.adj[u][v]
    return None

  def add_edge(self, u : Vertex, v : Vertex, w : float = 1.0) -> None:
    """
    Adds the vertices u, v into respective adjacency dicts.
    if u, v doesn't exist in graph, then new vertices u and v are added
    if graph is undirected, an edge (v,u) is also added to the graph
    """
    self.add_vertex(u)
    self.add_vertex(v)
    self.adj[u][v] = w
    if (not self.directed): self.adj[v][u] = w
  
  def remove_edge(self, u : Vertex, v : Vertex) -> None:
    """
    removes the v from the edge set of u
    if the graph was undirected, removes u from edge set of v
    """
    if v in self.adj[u]:
      del self.adj[u][v]
      if ((not self.directed) and (u in self.adj[v])): del self.adj[v][u]
    return None
  
  def get_out_deg(self, v : Vertex) -> int:
    """
    returns sum of outgoing edges from the vertex v
    if v does not exist, returns 0 by default
    """
    if v in self.adj: return len(self.adj[v])
    return 0

  def get_in_deg(self, v : Vertex) -> int:
    """
    returns sum of incoming edges into vertex v
    if v does not exist, returns 0 by default
    """      
    return sum([1 if (v in self.adj[u]) else 0 for u in self.adj])

  def get_out_neighbor(self, v : Vertex) -> iter:
    """
    returns an iterator over the dictionary of outgoing edges of vertex v
    if v does not exist in the graph, returns an empty iterator
    """
    if v in self.adj: return iter(self.adj[v])
    return iter([])
  
  def get_in_neighbor(self, v : Vertex) -> iter:
    """
    returns an iterator over the dictionary of incoming edges into vertex v
    if v does not exist in the graph, returns an empty iterator
    """
    return iter([u for u in self.adj if (v in self.adj[u])])
  
  def get_weight(self, u: Vertex, v : Vertex) -> float:
    """ returns the weight on edge (u, v)
        if edge (u,v) does not exist, returns None as weight
    """
    if u in self.adj: return self.adj[u][v]
    return None

  @property
  def T(self):
    """
    computes the transpose of a graph as described in CLRS Exercise 22.1-3
    O(V+E). returns a new graph that is transposed (edges reversed)
    """
    gt = AdjacencyDict(directed=self.directed)
    for u in self.adj.keys():
      for v, w in self.adj[u].items():
        gt.add_edge(v, u, w)
    return gt

  @property
  def n(self):
    """
    returns number of vertices in the graph
    """
    return len(self.adj)

  def __repr__(self) -> str:
    """
    prints the graph as an adjacency list representation
    """
    reps = [f'{v} : {[u for u in e.keys()]}\n' for v, e in self.adj.items()]
    rep = ''
    for r in reps: rep += r
    return rep

# def main():
#   dg = AdjacencyDict(directed=True)
#   dg.add_vertex(Vertex(1))
#   dg.add_vertex(Vertex(2))
#   dg.add_edge(Vertex(2), Vertex(3))
#   dg.add_edge(Vertex(2), Vertex(4), w=3)
#   dg.remove_vertex(Vertex(1))
#   dg.remove_edge(Vertex(2), Vertex(3))
#   print(dg)
#   G = AdjacencyDict(directed=True)
#   G.add_edge(Vertex(1), Vertex(2))
#   G.add_edge(Vertex(1), Vertex(4))
#   G.add_edge(Vertex(4), Vertex(2), w=2)
#   G.add_edge(Vertex(2), Vertex(5))
#   G.add_edge(Vertex(5), Vertex(4), w=7)
#   G.add_edge(Vertex(3), Vertex(5))
#   G.add_edge(Vertex(3), Vertex(6))
#   gt = G.T
#   print(set(gt.get_out_neighbor(Vertex(2))), gt.get_out_deg(Vertex(2)))
#   print(set(gt.get_in_neighbor(Vertex(2))), gt.get_in_deg(Vertex(2)))
#   g2 = gt.T
#   print(g2)
#   print(set(g2.get_out_neighbor(Vertex(2))), g2.get_out_deg(Vertex(2)))
#   print(set(g2.get_in_neighbor(Vertex(2))), g2.get_in_deg(Vertex(2)))

# if __name__=='__main__':
#   main()