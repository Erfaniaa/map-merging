from graph import Graph
import networkx as nx
from random import randint
import numpy as np

class GraphGenerator:

	def __init__(self):
		self.graph = None
		self.nodes_count = 0
		self.edges_count = 0

	def generate(self, min_nodes, max_nodes, min_edges, max_edges, min_xy, max_xy):
		graph = Graph()
		self.nodes_count = randint(min_nodes, max_nodes)
		self.edges_count = randint(min_edges, max_edges)
		self.edges_count = min(self.edges_count, 3 * self.nodes_count - 6)
		self.edges_count = max(self.edges_count, 0)
		for i in range(self.nodes_count):
			graph.add_node(i + 1)
		for i in range(self.edges_count):
			graph.add_edge(self._get_random_valid_edge())

	def _intersect(self, edge1, edge2):


	def _is_edge_valid(self, edge):
		return True

	def _get_random_edge(self):
		return None

	def _get_random_valid_edge(self):
		return None