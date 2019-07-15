import networkx as nx
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

from graph_node import Node
from polygon import Polygon

nodes = [
    Node(1, 10, 10),
    Node(2, 10, 20),
    Node(3, 20, 20),
    Node(4, 20, 10),
]

polygon = Polygon(nodes)
print(polygon.perimeter())

graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_edge(nodes[0], nodes[1])

# polygon.normalize()
plt.plot(polygon.turning_function())
plt.show()


# pos = {node: node.pos() for node in polygon.nodes}
# nx.draw(graph, pos)
# plt.show()
