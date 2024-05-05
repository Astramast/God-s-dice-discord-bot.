from Operator import *


class OperatorFactory():
    def __init__(self, char):
		self.operators = ["+", "-", "*", "/", "%", "d"]
		if char == "+":
			return Add
		elif char == "-":
			return Subtract
		elif char == "*":
			return Multiply
		elif char == "/":
			return Divide
		elif char == "%":
			return Modulo
		elif char == "d":
			return D
		else:
			raise ValueError("Invalid operator: " + char)

	def getOperators(self):
		return self.operators

