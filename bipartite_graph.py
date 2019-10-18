import networkx as nx
from vector import Vector

class BipartiteGraph:

    def __init__(self, nodes1=None, nodes2=None, edges=None):
        self.nodes1 = []
        self.nodes2 = []
        self.edges = []
        self.index_to_node = {}
        self.node_neighbors = {}
        if nodes1:
            self.nodes1 = nodes1
        if nodes2:
            self.nodes2 = nodes2
        if edges:
            self.edges = edges
            for edge in edges:
                if self.node_neighbors.get(edge.node1_index):
                    self.node_neighbors[edge.node1_index].append(edge.node2_index)
                else:
                    self.node_neighbors[edge.node1_index] = [edge.node2_index]
                if self.node_neighbors.get(edge.node2_index):
                    self.node_neighbors[edge.node2_index].append(edge.node1_index)
                else:
                    self.node_neighbors[edge.node2_index] = [edge.node1_index]

    def add_edge(self, edge):
        self.edges.append(edge)
        if self.node_neighbors.get(edge.node1_index):
            self.node_neighbors[edge.node1_index].append(node2_index)
        else:
            self.node_neighbors[edge.node1_index] = [node2_index]
        if self.node_neighbors.get(node2_index):
            self.node_neighbors[node2_index].append(edge.node1_index)
        else:
            self.node_neighbors[node2_index] = [edge.node1_index]

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
        if Edge(edge.node2_index, edge.node1_index, edge.weight) in self.edges:
            self.edges.remove((edge.node2_index, edge.node1_index, edge.weight))
        if edge.node2_index in self.node_neighbors.get(edge.node1_index, []):
            self.node_neighbors[edge.node1_index].remove(edge.node2_index)
        if edge.node1_index in self.node_neighbors.get(edge.node2_index, []):
            self.node_neighbors[edge.node2_index].remove(edge.node1_index)

    def add_node_to_part_one(self, node):
        self.nodes1.append(node)
        self.index_to_node[node.index] = node

    def add_node_to_part_two(self, node):
        self.nodes2.append(node)
        self.index_to_node[node.index] = node

    def get_maximum_weighted_matching(self):
        graph = nx.Graph()
        matching_graph = nx.Graph()
        for idx, node in enumerate(self.nodes1):
            graph.add_node(node.index, pos=(0, idx))
            matching_graph.add_node(node.index, pos=(0, idx))
        for idx, node in enumerate(self.nodes2):
            graph.add_node(node.index, pos=(20, idx))
            matching_graph.add_node(node.index, pos=(20, idx))
        for edge in self.edges:
            graph.add_edge(edge.node1_index, edge.node2_index, weight=edge.weight)
        matching_edges_set = nx.max_weight_matching(graph, maxcardinality=True)
        for node1, node2 in matching_edges_set:
            matching_graph.add_edge(node1, node2)
        return matching_graph

    def get_nx_graph(self):
        graph = nx.Graph()
        for idx, node in enumerate(self.nodes1):
            graph.add_node(node.index, pos=(0, idx))
        for idx, node in enumerate(self.nodes2):
            graph.add_node(node.index, pos=(20, idx))
        for edge in self.edges:
            graph.add_edge(edge.node1_index, edge.node2_index, weight=edge.weight)
        return graph
