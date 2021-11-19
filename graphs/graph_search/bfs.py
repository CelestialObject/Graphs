# given source vertex s, visit all reachable vertices
# O(V+E) time
# Single pair reachability: is there a path from s -> t
# Single pair shortest path: shortest distance from s->t and the shortest path
# single source shortest path: shortest dist from s->all v + corresponding paths
from dataclasses import dataclass, field
from graphs.graph import AdjacencyDict, Vertex

def bfs(G : AdjacencyDict, s : Vertex):
  pass


