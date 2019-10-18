import math
from vector import Vector


class Node:

    def __init__(self, index, x=None, y=None):
        self.index = index
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.index) + " " + str(self.x) + " " + str(self.y)

    def __repr__(self):
        return str(self.index) + " " + str(self.x) + " " + str(self.y)

    def get_pos_vector(self):
        return Vector(self.x, self.y)

    def distance(self, node):
        dx = node.x - self.x
        dy = node.y - self.y
        return math.hypot(dx, dy)

    def pos(self):
        return self.x, self.y

    def minus(self, node):
        return self.x - node.x, self.y - node.y
