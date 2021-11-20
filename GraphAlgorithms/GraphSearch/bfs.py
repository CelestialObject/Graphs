# given source vertex s, visit all reachable vertices
# O(V+E) time
# Single pair reachability: is there a path from s -> t
# Single pair shortest path: shortest distance from s->t and the shortest path
# single source shortest path: shortest dist from s->all v + corresponding paths
import queue
from dataclasses import dataclass, field
from ..Graph.graph import AdjacencyDict, Vertex

@dataclass
class BreadthFirstSearch:
  s : Vertex = field(default_factory=Vertex) # source vertex to start BFS
  d : dict = field(default_factory=dict) # distance from source vertex
  p : dict = field(default_factory=dict) # vertices parent to compute short path

  def traverse_graph(self, G : AdjacencyDict):
    """ Traverses the graph in BFS manner
    keeps track of d: distance from source vertex.
    keeps track of p: predecessor/parent of vertices in BFS tree
    """
    # initialize the BFS result, and set d[s] = 0, p[s] = None
    if (self.s not in G.adj):
      print('Source vertex not in Graph')
      return None
    self.d[self.s] = 0
    self.p[self.s] = None
    # initialize a queue to traverse vertices in G and put source vertex s in q
    Q = queue.Queue()
    Q.put(self.s)
    while(not Q.empty()):           # while queue is not empty
      u = Q.get()                   # get a vertex u
      for v in G.adj[u]:            # for all neighbors v of u
        if v not in self.d:         # if vertex v is unvisited
          self.d[v] = self.d[u] + 1 # d[u]++ and assign it to all d[v]
          self.p[v] = u             # set parent of v to u
          Q.put(v)                  # explore v next (so add it to queue)
    return None
  
  def get_levelset(self, i : int = None) -> dict:
    """ returns the level set (as computed by bfs on G from s)
    """
    level_set = {}
    for u, d in self.d.items():
      level_set.setdefault(d, set()).add(u)
    
    if (i is not None):
      if (i in level_set): return level_set[i]
      else:
        print(f'No vertices {i} levels away from {self.s}')
        return set() # return empty set
    return level_set
  
  def get_source(self) -> Vertex:
    return self.s

  def is_reachable(self, t : Vertex) -> bool:
    """ returns True if a path exists from s -> t
    """
    return (t in self.p)
  
  def get_shortest_path(self, t : Vertex) -> list:
    """ returns the optimal shortest path assuming non-weighted graph or 
        that weight on each edge is 1. returns an empty list if 
    """
    sp = []
    if (self.s == t): sp.append(self.s)
    elif (t not in self.p):
      print(f"No path exists from {self.s} to {t}")
      return []
    else:
      sp.extend(self.get_shortest_path(self.p[t]))
      sp.append(t)
    return sp

  def __repr__(self) -> str:
    """ Prints the level set as BFS representation
    """
    lvl_set = self.get_levelset()
    reps = [f'{d} : {l}\n' for d, l in lvl_set.items()]
    rep = ''
    for r in reps: rep += r
    return rep

# def main():
#   G = AdjacencyDict(directed=False)
#   G.add_edge(Vertex('a'), Vertex('z'))
#   G.add_edge(Vertex('a'), Vertex('s'))
#   G.add_edge(Vertex('s'), Vertex('x'))
#   G.add_edge(Vertex('x'), Vertex('d'))
#   G.add_edge(Vertex('x'), Vertex('c'))
#   G.add_edge(Vertex('d'), Vertex('c'))
#   G.add_edge(Vertex('d'), Vertex('f'))
#   G.add_edge(Vertex('c'), Vertex('f'))
#   G.add_edge(Vertex('c'), Vertex('v'))
#   G.add_edge(Vertex('f'), Vertex('v'))
#   print(G)
#   bfs_result = bfs(G, Vertex('s'))
#   print(bfs_result)
#   return 0

# if __name__=='__main__':
#   main()