import product as pd

class Salesperson:
	def __init__(self, name):
		"""
		return assign its value to a name attribute.
		"""
		self.name = name

	def __str__(self):
		"""
		return name attribute of the instance.
		"""
		return self.name

	def promote(self):
		"""
		return a Product instance.
		"""
		promo = pd.Product()
		return promo