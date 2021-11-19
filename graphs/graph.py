# --version > python3.10 is must 
# My implementation of graphs and graph algorithms
import sys
import numpy as np
from typing import Any
from dataclasses import dataclass, field

from numpy.lib.function_base import iterable

@dataclass(frozen=True, order=True)
class Vertex:
  item : Any

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
    return sum([1 if (v in self.adj[u]) else 0 for u in self.adj.keys()])

  def get_neighbor(self, v : Vertex) -> iter:
    """
    returns an iterator over the dictionary of outgoing edges of vertex v
    if v does not exist in the graph, returns an empty iterator
    """
    if v in self.adj: return iter(self.adj[v])
    return iter([])

  @property
  def n(self):
    """
    returns number of vertices in the graph
    """
    return len(self.adj)
  
  # @property
  # def m(self):
  #   """
  #   returns number of edges in the graph
  #   """
  #   return sum([len(self.adj[u]) for u in self.adj.keys()])

  def __str__(self) -> str:
    """
    prints the graph as an adjacency list representation
    """
    reps = [f'{v} : {e.keys()}\n' for v, e in self.adj.items()]
    rep = ''
    for r in reps: rep += r
    return rep

def main():
  G = AdjacencyDict()
  # for i in range(1, 7):
  #   G.add_vertex(Vertex(i))
  G.add_edge(Vertex(1), Vertex(2))
  G.add_edge(Vertex(1), Vertex(5))
  G.add_edge(Vertex(5), Vertex(2))
  G.add_edge(Vertex(2), Vertex(4))
  G.add_edge(Vertex(5), Vertex(4))
  G.add_edge(Vertex(3), Vertex(2))
  G.add_edge(Vertex(3), Vertex(4))
  print(sys.getsizeof(G))
  print(G.n, G.m)
  # print(set(G.get_neighbor(Vertex(2))))
  # print(set(G.get_neighbor(Vertex(7))))
  # print(G.get_out_deg(Vertex(1)))
  # print(G.get_out_deg(Vertex(6)))
  # print(G.get_out_deg(Vertex(5)))
  # print(G.get_out_deg(Vertex(2)))
  # print(G.get_in_deg(Vertex(6)))
  # print(G.get_in_deg(Vertex(5)))
  # print(G.get_in_deg(Vertex(2)))
  # print(G.get_in_deg(Vertex(4)))
  # print(G.get_in_deg(Vertex(3)))

if __name__=='__main__':
  main()