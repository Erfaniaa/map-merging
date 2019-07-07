import networkx as nx
from matplotlib import pyplot as plt
from node import Node

graph = nx.Graph()
node1, node2 = Node(1, 10, 10), Node(2, 20, 20)

graph.add_node(1, pos=(10, 10))
graph.add_node(2, pos=(20, 20))

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
