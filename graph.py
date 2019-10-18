import networkx as nx
from vector import Vector
from polygon import Polygon

class Graph:

    def __init__(self, nodes=None, edges=None):
        self.nodes = []
        self.edges = []
        self.index_to_node = {}
        self.node_neighbors = {}
        if nodes:
            self.nodes = nodes
        if edges:
            self.edges = edges
            for edge in edges:
                if self.node_neighbors.get(edge[0]):
                    self.node_neighbors[edge[0]].append(edge[1])
                else:
                    self.node_neighbors[edge[0]] = [edge[1]]
                if self.node_neighbors.get(edge[1]):
                    self.node_neighbors[edge[1]].append(edge[0])
                else:
                    self.node_neighbors[edge[1]] = [edge[0]]

    def add_edge(self, edge):
        self.edges.append(edge)
        if self.node_neighbors.get(edge[0]):
            self.node_neighbors[edge[0]].append(edge[1])
        else:
            self.node_neighbors[edge[0]] = [edge[1]]
        if self.node_neighbors.get(edge[1]):
            self.node_neighbors[edge[1]].append(edge[0])
        else:
            self.node_neighbors[edge[1]] = [edge[0]]

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
        if (edge[1], edge[0]) in self.edges:
            self.edges.remove((edge[1], edge[0]))
        if edges[1] in self.node_neighbors.get(edges[0], []):
            self.node_neighbors[edges[0]].remove(edges[1])
        if edges[0] in self.node_neighbors.get(edges[1], []):
            self.node_neighbors[edges[1]].remove(edges[0])

    def add_node(self, node):
        self.nodes.append(node)
        self.index_to_node[node.index] = node

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
            self.polar_sort_node_neighbors(node, self.node_neighbors.get(node, []))

    def get_face_of_edge(self, edge):
        first_edge = edge
        face_edges = []
        edge = self.get_next_edge_in_face(edge[0], edge[1])
        face_edges.append(self.index_to_node[edge[0]])
        while edge and edge != first_edge:
            edge = self.get_next_edge_in_face(edge[0], edge[1])
            face_edges.append(self.index_to_node[edge[0]])
        return Polygon(nodes=face_edges)

    def get_next_edge_in_face(self, node, prev_node):
        node_neighbors = self.node_neighbors[node].copy()
        node_neighbors.sort(key=lambda v: Vector(self.nodes[v].x - self.nodes[node].x, self.nodes[v].y - self.nodes[node].y).get_angle())
        node_neighbors_count = len(node_neighbors)
        last_neighbor = node_neighbors[-1]
        for neighbor in node_neighbors:
            if neighbor == prev_node:
                return (last_neighbor, node)
            last_neighbor = neighbor

    def get_node_adjacent_faces(self, node):
        faces = []
        for neighbor in self.node_neighbors.get(node, []):
            faces.append(self.get_face_of_edge((node, neighbor)))
        return faces

    def get_all_graph_faces(self):
        graph_faces = []
        for node in self.nodes:
            graph_faces.append(self.get_node_adjacent_faces(node.index))
        return graph_faces
