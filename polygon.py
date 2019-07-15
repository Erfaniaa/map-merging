from graph_node import Node
import math
import numpy as np


class Polygon:
    nodes = None  # type: list[Node]

    TF_POINTS = 1000

    def __init__(self, nodes):
        self.nodes = nodes
        self.tf = None

    def edges(self):
        for i in range(len(self.nodes) - 1):
            yield (self.nodes[i], self.nodes[i + 1])
        yield (self.nodes[-1], self.nodes[0])

    def normalize(self):
        """ scale nodes so that perimeter becomes one """
        p = self.perimeter()
        for node in self.nodes:
            node.x /= p
            node.y /= p

    def perimeter(self):
        p = 0
        for n1, n2 in self.edges():
            p += n1.distance(n2)
        return p

    def turning_function(self):
        if self.tf:
            return self.tf
        tf = [0] * self.TF_POINTS
        p = 0
        total_p = self.perimeter()
        last_set_id = -1
        for n1, n2 in self.edges():
            final_p = p + n1.distance(n2)
            last = int(final_p / total_p * self.TF_POINTS)
            for i in range(last_set_id + 1, min(last + 1, self.TF_POINTS)):
                dx, dy = n2.minus(n1)
                # print(i)
                tf[i] = math.atan2(dy, dx) / math.pi

            last_set_id = last
            p = final_p

        self.tf = tf
        return tf

    def distance(self, polygon):
        pass
