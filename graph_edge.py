class Edge:

	def __init__(self, node1_index, node2_index, weight=0):
		self.node1_index = node1_index
		self.node2_index = node2_index
		self.weight = weight

	def __str__(self):
		return str(self.node1_index) + " " + str(self.node2_index) + " " + str(int(self.weight))

	def __repr__(self):
		return str(self.node1_index) + " " + str(self.node2_index) + " " + str(int(self.weight))

