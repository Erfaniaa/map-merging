from graph import Graph
import networkx as nx
from math import acos, sin, cos, pi
from random import randint, random
import numpy as np
from graph_node import Node

class GraphGenerator:

	def __init__(self):
		self.graph = None
		self.nodes_count = 0
		self.edges_count = 0

	def generate(self, min_nodes, max_nodes, min_edges, max_edges, min_xy, max_xy):
		self.graph = Graph()
		self.nodes_count = randint(min_nodes, max_nodes)
		self.edges_count = randint(min_edges, max_edges)
		self.edges_count = min(self.edges_count, 3 * self.nodes_count - 6)
		self.edges_count = max(self.edges_count, 0)
		for i in range(self.nodes_count):
			self.graph.add_node(Node(i, randint(min_xy, max_xy), randint(min_xy, max_xy)))
		for i in range(self.edges_count):
			edge = self._get_random_valid_edge()
			if edge:
				self.graph.add_edge(edge)
			else:
				break
		return self.graph

	def generate_circular(self, min_nodes, max_nodes, min_edges, max_edges, radius):
		self.graph = Graph()
		self.nodes_count = randint(min_nodes, max_nodes)
		self.edges_count = randint(min_edges, max_edges)
		self.edges_count = min(self.edges_count, 3 * self.nodes_count - 6)
		self.edges_count = max(self.edges_count, 0)
		for i in range(self.nodes_count):
			theta = i / self.nodes_count * 2 * pi
			x, y = int(radius * cos(theta)), int(radius * sin(theta))
			self.graph.add_node(Node(i, x, y))
		for i in range(self.edges_count):
			edge = self._get_random_valid_edge()
			if edge:
				self.graph.add_edge(edge)
			else:
				break
		return self.graph

	def remove_edge(self, node1, node2):
		if (node1, node2) in self.graph.edges:
			self.graph.edges.remove((node1, node2))
			self.nodes_count -= 1
		if (node2, node1) in self.graph.edges:
			self.graph.edges.remove((node2, node1))
			self.nodes_count -= 1
		if self.graph.node_neighbors.get(node1):
			self.graph.node_neighbors[node1].remove(node2)
			self.nodes_count -= 1
		if self.graph.node_neighbors.get(node2):
			self.graph.node_neighbors[node2].remove(node1)
			self.nodes_count -= 1

	def remove_random_edges(self, min_edges_to_remove, max_edges_to_remove):
		number_of_edges_to_remove = randint(min_edges_to_remove, max_edges_to_remove)
		number_of_edges_to_remove = min(number_of_edges_to_remove, self.edges_count)
		number_of_edges_to_remove = max(number_of_edges_to_remove, 0)
		graph_edges_copy = self.graph.edges.copy()
		for i in range(number_of_edges_to_remove):
			self.remove_edge(graph_edges_copy[i][0], graph_edges_copy[i][1])

	def change_node_position(self, node, max_xy_change):
		x_diff = randint(0, 2 * max_xy_change + 1) - max_xy_change
		y_diff = randint(0, 2 * max_xy_change + 1) - max_xy_change
		node.x += x_diff
		node.y += y_diff

	def change_all_nodes_position(self, max_xy_change):
		for node in self.graph.nodes:
			self.change_node_position(node, max_xy_change)

	def _intersect(self, edge1, edge2):
		if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
			return False
		if edge1[1] == edge2[0] or edge1[1] == edge2[1]:
			return False
		vector1 = self.graph.nodes[edge2[0]].get_pos_vector() - self.graph.nodes[edge1[0]].get_pos_vector()
		vector2 = self.graph.nodes[edge2[1]].get_pos_vector() - self.graph.nodes[edge1[0]].get_pos_vector()
		vector3 = self.graph.nodes[edge2[0]].get_pos_vector() - self.graph.nodes[edge1[1]].get_pos_vector()
		vector4 = self.graph.nodes[edge2[1]].get_pos_vector() - self.graph.nodes[edge1[1]].get_pos_vector()
		if vector1.cross(vector2) * vector3.cross(vector4) <= 0:
			return True
		if vector3.cross(vector1) * vector4.cross(vector2) <= 0:
			return True
		return False

	def _is_edge_valid(self, edge):
		for other_edge in self.graph.edges:
			if edge == other_edge or (edge[0] == other_edge[1] and edge[1] == other_edge[0]) or self._intersect(edge, other_edge):
				return False
		return True

	def _get_random_edge(self):
		x, y = randint(0, self.nodes_count - 1), randint(0, self.nodes_count - 1)
		while x == y:
			x, y = randint(0, self.nodes_count - 1), randint(0, self.nodes_count - 1)
		return (x, y)

	def _get_random_valid_edge(self):
		random_edge = self._get_random_edge()
		cnt = 0
		while not self._is_edge_valid(random_edge):
			cnt += 1
			if cnt == 100:
				return None
			random_edge = self._get_random_edge()
		return random_edge
