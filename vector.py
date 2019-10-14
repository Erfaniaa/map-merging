from math import atan2


class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __sub__(self, v):
		return Vector(self.x - v.x, self.y - v.y)

	def __add__(self, v):
		return Vector(self.x + v.x, self.y + v.y)

	def cross(self, v):
		return self.x * v.y - v.x * self.y

	def dot(v):
		return self.x * v.x + v.y * self.y

	def get_angle(self):
		return atan2(self.y, self.x)

	def get_length(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

