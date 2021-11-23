# Copyright, Aman Gupta - November 2020
from dataclasses import dataclass, field

@dataclass(slots=True)
class AdjacencyDict:
  """ A dictionary of dictionaries.
      sparse representation of an Adjacency Matrix
      data-structure: adj[k] = {val_k : val_v}
      eg. G = (V, E) -> G.adj[u] = {v : w}, where (u,v): edge in G with weight w
  """
  adj : dict = field(default_factory=dict)

  def add_key(self, k) -> None:
    """ Adds key k into the adj dictionary.
        Assigns an empty dictionary as its value
        Assumes k is an immutable data-type, so make classes frozen!
    """
    if (k not in self.adj): self.adj.setdefault(k, dict())
    return None
  
  def set_value(self, k, val_k, val_v) -> None:
    """ Assumes val is a dictionary item -> (val_key : val_val) pair
        if key k does not exist in adj, a new key k is created
        assumes val_k is immutable data type
        val_k added only if it does not already exist in self.adj[k]
    """
    self.add_key(k)
    if (val_k not in self.adj[k]): self.adj[k][val_k] = val_v
    return None
  
  def get_value(self, k, val_k):
    if k in self.adj:
      if val_k in self.adj[k]:
        return self.adj[k][val_k]
    return None

  def has_key(self, k):
    return (k in self.adj)
  
  def delete_key(self, k) -> None:
    """ deletes key k from adj dictionary (only if k exists in adj)
    """
    if self.has_key(k): del self.adj[k]
    return None
  
  def has_valk(self, val_k, k=None) -> bool:
    if ((k is not None) and (self.has_key(k))):
      return val_k in self.adj[k]

  def delete_valk(self, val_k, k=None) -> None:
    """ if k is provided, only adj[k][val_k] is deleted, if k and val_k exists
        else: deletes the val_k key in any value dict for all keys k in adj
    """
    if self.has_valk(val_k, k):
        del self.adj[k][val_k]
        return None
    else:
      for k, val in self.adj.items():
        if val_k in val: del self.adj[k][val_k]
    return None

  def get_adj(self, k) -> iter:
    if (k in self.adj): return self.adj[k]
    return {}

  @property # number of keys. eg: number of vertices in a graph
  def n(self):
    return len(self.adj)
  
  @property # number of values associated to all keys, eg: number of edges
  def m(self):
    return sum([len(self.adj[u]) for u in self.adj])

  def __repr__(self) -> str:
    reps = [f'{k} : {[(vk, v[vk]) for vk in v.keys()]}\n'\
            for k, v in self.adj.items()]
    rep = ''
    for r in reps: rep += r
    return rep

# @dataclass(slots=True)
# class AdjacencyMatrix(AdjacencyDict):
#   pass