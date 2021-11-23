import unittest

from ..Graph.graph import Graph, Vertex, Edge

class TestGraphCreation(unittest.TestCase):
  def test_vertex_creation(self):
    G = Graph()
    n = G.n
    self.assertIs(n, 0)

    u = Vertex(1)
    self.assertIsInstance(u, Vertex)

    G.add_vertex(u) # test for adding vertex to an empty graph
    n += 1 # n = 1
    self.assertIs(G.n, 1)
    self.assertTrue(G.has_vertex(u))
    self.assertIsInstance(G.get_adj(u), dict)
    self.assertIs(len(G.get_adj(u)), 0)

    v = Vertex(2) 
    G.add_vertex(v) # test for adding a vertex in a non-empty graph
    n += 1 # n = 2
    self.assertIs(G.n, n)
    self.assertTrue(G.has_vertex(v))
    self.assertIsInstance(G.get_adj(v), dict)
    self.assertIs(len(G.get_adj(v)), 0)

    w = Vertex(2) # test for not adding duplicates 
    G.add_vertex(w)
    self.assertIs(G.n, n)
    self.assertTrue(G.has_vertex(w))
    self.assertIsNotNone(G.get_adj(w))
    self.assertIsInstance(G.get_adj(w), dict)
    self.assertIs(len(G.get_adj(w)), 0)
  
  def test_edge_creation(self):
    G1 = Graph(directed=True)
    G2 = Graph()
    u = Vertex(1)
    v = Vertex(2)
    w = Vertex(3)

    G1.add_edge(u, v) # test for adding edge to an empty graph directed
    G2.add_edge(u, v) # undirected graph
    # tests for existence of vertices in edges and updates of graph parameters
    self.assertIs(G1.n, 2)
    self.assertIs(G2.n, 2)
    self.assertIs(G1.m, 1)
    self.assertIs(G2.m, 2)

    self.assertTrue(G1.has_vertex(u))
    self.assertTrue(G1.has_vertex(v))
    self.assertTrue(G2.has_vertex(u))
    self.assertTrue(G2.has_vertex(v))
    
    # test for graph representation as adjacency dicts
    self.assertIsInstance(G1.get_adj(u), dict)
    self.assertIs(len(G1.get_adj(u)), 1)
    self.assertIs(len(G1.get_adj(v)), 0)

    self.assertIsInstance(G2.get_adj(u), dict)
    self.assertIs(len(G2.get_adj(u)), 1)
    self.assertIs(len(G2.get_adj(v)), 1)

    # adding a weighted edge
    G1.add_edge(u, w, e=Edge(w=2))
    G2.add_edge(u, w, e=Edge(w=2))
    self.assertIs(G1.n, 3)
    self.assertIs(G2.n, 3)
    self.assertIs(G1.m, 2)
    self.assertIs(G2.m, 4)
    self.assertTrue(G1.has_vertex(w))
    self.assertTrue(G2.has_vertex(w))
    self.assertIsNotNone(G1.get_weight(u, w))
    self.assertIsNotNone(G2.get_weight(u, w))
    self.assertIs(G1.get_weight(u, w), 2)
    self.assertIs(G2.get_weight(u, w), 2)

  def test_vertex_removal(self):
    G1 = Graph(directed=True)
    G2 = Graph()
    G1.remove_vertex(Vertex(1)) # removing a vertex from an empty graph
    G2.remove_vertex(Vertex(1))
    self.assertIs(G1.n, 0)
    self.assertFalse(G1.has_vertex(Vertex(1)))
    self.assertIs(G2.n, 0)
    self.assertFalse(G2.has_vertex(Vertex(1)))

    u = Vertex(1)
    v = Vertex(2)
    w = Vertex(3)
    x = Vertex(4)
    G1.add_vertex(u) 
    G1.add_vertex(v)
    G1.add_vertex(w)
    G2.add_vertex(u) 
    G2.add_vertex(v)
    G2.add_vertex(w)
    n = G1.n
    self.assertIs(G1.n, 3)
    self.assertIs(G2.n, 3)

    G1.remove_vertex(v)
    G2.remove_vertex(v)
    self.assertIs(G1.n, 2)
    self.assertIs(G2.n, 2)
    self.assertFalse(G1.has_vertex(v))
    self.assertFalse(G2.has_vertex(v))

    G1.add_edge(u, v)
    G1.add_edge(u, w)
    G1.add_edge(u, x)
    G2.add_edge(u, v)
    G2.add_edge(u, w)
    G2.add_edge(u, x)
    self.assertIs(G1.n, 4)
    self.assertIs(G1.m, 3)
    self.assertIs(G2.n, 4)
    self.assertIs(G2.m, 6)

    G1.remove_vertex(u)
    G2.remove_vertex(u)
    self.assertIs(G1.n, 3)
    self.assertIs(G1.m, 0)
    self.assertIs(G2.n, 3)
    self.assertIs(G2.m, 0)
    self.assertFalse(G1.has_vertex(u))
    self.assertFalse(G2.has_vertex(u))
  
  def test_edge_removal(self):
    G1 = Graph(directed=True)
    G2 = Graph()
    u, v, w = Vertex(1), Vertex(2), Vertex(3)
    G1.add_edge(u, v)
    G1.add_edge(v, u)
    G1.add_edge(u, w)
    G1.add_edge(w, v)
    G2.add_edge(u, v)
    G2.add_edge(u, w)
    G2.add_edge(w, v)
    G2.add_edge(v, w)
    self.assertIs(G1.n, 3)
    self.assertIs(G2.n, 3)
    self.assertIs(G1.m, 4)
    self.assertIs(G2.m, 6)
    G1.remove_edge(u,v)
    G2.remove_edge(u,v)
    self.assertIs(G1.n, 3)
    self.assertIs(G2.n, 3)
    self.assertIs(G1.m, 3)
    self.assertIs(G2.m, 4)
    self.assertFalse(G1.has_edge(u, v))
    self.assertFalse(G2.has_edge(u, v))


if __name__=='__main__':
  unittest.main()