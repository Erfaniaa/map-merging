from graph_node import Node
import math
import numpy as np


class MapMerger:
    
    def __init__(self):
        self.graph_generator = GraphGenerator()
        self.graph1 = self.graph_generator.generate_circular(15, 15, 3 * 15 - 6, 3 * 15 - 6, 50)
        self.graph1.polar_sort_all_graph_edges()        
        self.nx_graph1 = self.graph1.get_nx_graph()
        self.graph_generator.remove_random_edges(3, 7)
        self.graph_generator.change_all_nodes_position(2)
        self.graph2 = graph_generator.graph
        self.nx_graph2 = self.graph2.get_nx_graph()
        part_one = self.graph1.nodes.copy()
        part_two = self.graph2.nodes.copy()
        edges = []
        for node in part_one:
            node.index = node.index * 10 + 0
        for node in part_two:
            node.index = node.index * 10 + 1
        for node1 in part_one:
            node1_prev_index = node1.index // 10
            node1_adjacent_faces = Polygons(polygons=self.graph1.get_node_adjacent_faces(node1_prev_index))
            turning_function1 = node1_adjacent_faces.get_all_polygons_turning_function()
            for node2 in part_two:
                node2_prev_index = node2.index // 10
                turning_function2 = node2_adjacent_faces.get_all_polygons_turning_function()
                edges.append(Edge(node1.index, node2.index, self._turning_functions_similarity(turning_function1, turning_function2)))
        self.bipartite_graph = BipartiteGraph(part_one, part_two, edges)

    def _turning_functions_similarity(self, turning_function1, turning_function2):
        length = min(len(turning_function1), len(turning_function2))
        ret = 360 * length
        for i in range(length):
            ret -= abs(turning_function1[i] - turning_function2[i])
        return ret

    def show(self):
        pos1 = nx.get_node_attributes(self.nx_graph1, 'pos')
        pos2 = nx.get_node_attributes(self.nx_graph2, 'pos')
        pos3 = nx.get_node_attributes(self.bipartite_nx_graph, 'pos')
        plt.figure(1)
        nx.draw(self.nx_graph1, pos1, with_labels=True)
        plt.figure(2)
        nx.draw(self.nx_graph2, pos2, with_labels=True)
        plt.figure(3)
        plt.show()


map_merger = MapMerger()
map_merger.show()
