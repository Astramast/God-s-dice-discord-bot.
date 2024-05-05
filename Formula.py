from FormulaComponent import Number
from OperatorFactory import OperatorFactory
from collections import deque


class Formula:
	def __init__(self, formula):
		self.root = self.parse(formula)

	def evaluate(self):
		return self.root.getValue()

	def __str__(self):
		return str(self.root)

	def parse(self, formula):
		head = 0
		number = ""
		factory = OperatorFactory()
		operators = factory.getOperators()
		while head < len(formula):
			char = formula[head]
			if char.isdigit():
				number += char
				continue
			else:
				root = Number(int(number))
				number = ""
			if char in operators:
				root = factory.getOperator(char)(root, self.parse(formula[head + 1:]))
			head += 1
		return root

