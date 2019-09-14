import networkx as nx
from matplotlib import pyplot as plt
from graph_node import Node
from vector import Vector
from math import atan2

graph = nx.Graph()
node1, node2 = Node(1, 10, 10), Node(2, 20, 20)

graph.add_node(node1.index, pos=(node1.x, node1.y))
graph.add_node(node2.index, pos=(node2.x, node2.y))

print(graph.nodes[1]['pos'])
print(graph.nodes[2]['pos'])

graph.add_edge(1, 2)

print("Nodes of graph: ")
print(graph.nodes())
print("Edges of graph: ")
print(graph.edges())

pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos)
plt.show()


class Graph:

    def __init__(self, nodes=None, edges=None):
        self.nodes = []
        self.edges = []
        self.node_neighbors = {}
        if nodes:
            self.nodes = nodes
        if edges:
            self.edges = edges
            for edge in edges:
            	if self.node_neighbors.get(edge[0]):
            		self.node_neighbors[edge[0]].append(edge[1])
            	else:
            		self.node_neighbors[edge[0]] = []
            	if self.node_neighbors.get(edge[1]):
            		self.node_neighbors[edge[1]].append(edge[0])
            	else:
            		self.node_neighbors[edge[1]] = []

    def add_edge(self, edge):
		self.edges.append(edge)
		if self.node_neighbors.get(edge[0]):
    		self.node_neighbors[edge[0]].append(edge[1])
    	else:
    		self.node_neighbors[edge[0]] = []
    	if self.node_neighbors.get(edge[1]):
    		self.node_neighbors[edge[1]].append(edge[0])
    	else:
    		self.node_neighbors[edge[1]] = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_nx_graph(self):
        graph = nx.Graph()
        for node in self.nodes:
            graph.add_node(node.index, pos=(node.x, node.y))
        for edge in self.edges:
            graph.add_edge(edge[0], edge[1])
        return graph

    def polar_sort_node_neighbors(self, node, neighbors):
    	neighbors.sort(key=lambda v: Vector(v.x - node.x, v.y - node.y).get_angle())
    	return neighbors

    def polar_sort_all_graph_edges(self):
    	for node in self.nodes:
    		self.polar_sort_node_neighbors(node, self.node_neighbors)

    def get_face_of_edge(self, edge):
    	first_edge = edge
    	face_edges = []
    	edge = get_next_edge_in_face(edge)
    	face_edges.append(edge)
    	while edge != first_edge:
    		edge = get_next_edge_in_face(edge)
    		face_edges.append(edge)
    	return face_edges

    def get_next_edge_in_face(self, node, prev_node):
    	node_neighbors = self.node_neighbors[node].copy()
    	edges.append(prev_node)
    	node_neighbors.sort(key=lambda v: Vector(v.x - node.x, v.y - node.y).get_angle())
    	node_neighbors_count = len(node_neighbors)
    	last_neighbor = node_neighbors[-1]
    	for neighbor in node_neighbors:
    		if neighbor == node:
    			return (node, last_neighbor)
    		last_neighbor = neighbor

    def get_node_adjacent_faces(self, node):
    	faces = []
    	for neighbor in self.node_neighbors[node]:
    		faces.append(get_face_of_edge((node, neighbor)))
    	return faces

    def get_all_graph_faces(self):
    	graph_faces = []
    	for node in nodes:
    		graph_faces.append(get_node_adjacent_faces(node))
    	return graph_face
