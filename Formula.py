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
		queue = deque()
		factory = OperatorFactory()
		operators = factory.getOperators()
		while head < len(formula):
			char = formula[head]
			if char == "(":
				last = formula.rfind(")")
				self.root = self.parse(formula[head:last + 1])
				head = last + 1
			elif char in operators:
				number = Number(int("".join(queue)))
				queue.clear()
			queue.append(char)
			head += 1
