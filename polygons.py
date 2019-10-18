from graph_node import Node
import math
import numpy as np


class Polygons:
    polygons = None  # type: list[Polygon]

    TF_POINTS = 10000

    def __init__(self, polygons):
        self.polygons = polygons

    def get_all_polygons_turning_function(self):
        if (not self.polygons) or (len(self.polygons) == 0):
            return [0] * self.TF_POINTS
        else:
            current_polygon_index = 0
            current_polygon_turning_function = self.polygons[current_polygon_index].turning_function()
            current_polygon_turning_function_index = 0
            polygons_count = len(self.polygons)
            turning_function = [0] * self.TF_POINTS
            for i in range(self.TF_POINTS):
                if current_polygon_index != (i * polygons_count) // self.TF_POINTS:
                    current_polygon_index = (i * polygons_count) // self.TF_POINTS
                    current_polygon_turning_function = self.polygons[current_polygon_index].turning_function()
                current_polygon_turning_function_index = (i * polygons_count) % self.TF_POINTS
                turning_function[i] = current_polygon_turning_function[current_polygon_turning_function_index]
            return turning_function