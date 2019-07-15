import math


class Node:

    def __init__(self, index, x=None, y=None):
        self.index = index
        self.x = x
        self.y = y

    def distance(self, node):
        dx = node.x - self.x
        dy = node.y - self.y
        return math.hypot(dx, dy)

    def pos(self):
        return self.x, self.y

    def minus(self, node):
        return self.x - node.x, self.y - node.y
