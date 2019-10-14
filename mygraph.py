import networkx as nx
from matplotlib import pyplot as plt
from graph_node import Node
from vector import Vector
from math import atan2
from graph_generator import GraphGenerator
from graph import Graph

graph_generator = GraphGenerator()
graph1 = graph_generator.generate_circular(15, 15, 3 * 15 - 6, 3 * 15 - 6, 50)
nx_graph1 = graph1.get_nx_graph()

graph_generator.remove_random_edges(3, 7)
graph_generator.change_all_nodes_position(2)
graph2 = graph_generator.graph
nx_graph2 = graph2.get_nx_graph()

node1, node2, node3, node4 = Node(0, 10, 10), Node(1, 10, 20), Node(2, 20, 20), Node(3, 20, 10)
# graph = Graph([node1, node2, node3, node4], [(0, 1), (1, 2), (2, 3), (3, 0)])

# nx_graph1.add_node(node1.index, pos=(node1.x, node1.y))
# nx_graph1.add_node(node2.index, pos=(node2.x, node2.y))
# nx_graph1.add_node(node3.index, pos=(node3.x, node3.y))
# nx_graph1.add_node(node4.index, pos=(node4.x, node4.y))

# nx_graph1.add_edge(1, 2)
# nx_graph1.add_edge(2, 3)
# nx_graph1.add_edge(3, 4)
# nx_graph1.add_edge(4, 1)

print("Nodes of graph: ")
print(nx_graph1.nodes())
print("Edges of graph: ")
print(nx_graph1.edges())

graph1.polar_sort_all_graph_edges()

# print(graph.get_node_adjacent_faces(0))
# print(graph.get_node_adjacent_faces(1))
# print(graph.get_node_adjacent_faces(2))
# print(graph.get_node_adjacent_faces(3))


# print(graph1.get_all_graph_faces())

pos1 = nx.get_node_attributes(nx_graph1, 'pos')
pos2 = nx.get_node_attributes(nx_graph2, 'pos')
plt.figure(1)
nx.draw(nx_graph1, pos1, with_labels=True)
plt.figure(2)
nx.draw(nx_graph2, pos2, with_labels=True)
plt.show()
