# Copyright, Aman Gupta - November 2020
from typing import Any
from dataclasses import dataclass, field
from GraphAlgorithms.Graph.adjacency_relations import AdjacencyDict

@dataclass(frozen=True, order=True, slots=True)
class Vertex:
  item : Any
  def __repr__(self) -> str:
    return str(self.item)

@dataclass(order=True, slots=True)
class Edge:
  w : float = 1
  dfs_t : str = field(compare=False, default_factory=str)

  def __repr__(self) -> str:
    return f'{self.w}, {self.dfs_t}'

@dataclass(repr=False, slots=True)
class Graph(AdjacencyDict):
  weighted : bool = False
  directed : bool = False

  def add_vertex(self, v: Vertex) -> None:
    """ Add vertex v as a key in an AdjacencyDict: adj
    """
    self.add_key(v)
    return None
  
  def remove_vertex(self, v: Vertex) -> None:
    """ remove v from the adj keys. 
        remove v from any outgoing edge of u for any u!=v in adj
    """
    self.delete_key(v) # O(1) : remove vertex from G
    self.delete_valk(v) # O(V) : remove vertex from all outgoing neighbor sets
    return None
  
  def has_vertex(self, v: Vertex) -> bool:
    return self.has_key(v)

  def add_edge(self, u: Vertex, v: Vertex, e_data: Edge = Edge()) -> None:
    """ if u, v does not exist in graph (as keys in adj) then add vertices u, v
    set edge e data to adj[u][v], if undirected: also set edge e to adj[v][u]
    """
    if (e_data.w != 1): self.weighted = True
    self.add_vertex(u)
    self.add_vertex(v)
    self.set_value(u, v, e_data)
    if (not self.directed): self.set_value(v, u, e_data)
    return None
  
  def remove_edge(self, u: Vertex, v: Vertex) -> None:
    """ remove v from adj[u]. if G undirected: remove u from adj[v]
    """
    self.delete_valk(k=u, val_k=v)
    if (not self.directed): self.delete_valk(k=v, val_k=u)
    return None
  
  def has_edge(self, u: Vertex, v: Vertex) -> bool:
    if (not self.directed):
      return ((self.has_valk(u, v)) and (self.has_valk(v, u)))
    return self.has_valk(u, v)

  def get_weight(self, u: Vertex, v: Vertex) -> float:
    return self.get_value(u, v).w

  @property # iterater over the set of all vertices in the graph: G.V
  def V(self) -> iter:
    return self.get_keys()
  
  @property
  def T(self):
    """
    computes the transpose of a graph as described in CLRS Exercise 22.1-3
    O(V+E). returns a new graph that is transposed (edges reversed)
    """
    if (not self.directed): return self
    Gt = Graph(directed=self.directed)
    for u in self.V:
      for v, e_data in self.get_adj(u).items():
        Gt.add_edge(v, u, e_data)
    return Gt
