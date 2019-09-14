from math import atan2


class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def minus(v):
		return Vector(x - v.x, y - v.y)

	def add(v):
		return Vector(x + v.x, y + v.y)

	def cross(v):
		return x * v.y - v.x * y

	def dot(v):
		return x * v.x + v.y * y

	def get_angle():
		return atan2(y, x)

	def get_length():
		return (x ** 2 + y ** 2) ** 0.5

