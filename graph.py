import networkx as nx
from matplotlib import pyplot as plt
from node import Node

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
		if nodes:
			self.nodes = nodes
		if edges:
			self.edges = edges

	def add_edge(self, edge):
		self.edges.append(edge)

	def add_node(self, node):
		self.nodes.append(node)

	def get_nx_graph(self):
		graph = nx.Graph()
		for node in nodes:
			graph.add_node(node.index, pos=(node.x, node.y))
		for edge in edges:
			graph.add_edge(edge[0], edge[1])
		return graph
