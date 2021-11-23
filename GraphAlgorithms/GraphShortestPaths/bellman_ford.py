from dataclasses import dataclass
from ..Graph.graph import AdjacencyDict, Vertex
from GraphAlgorithms.GraphShortestPaths.shortest_path import ShortestPath

@dataclass
class BellmanFord(ShortestPath):
  def get_negative_weight_cycle(self):
    pass