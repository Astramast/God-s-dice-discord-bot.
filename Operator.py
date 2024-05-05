from Dice import DiceBucket
from Formula import FormulaComponent


class Operator(FormulaComponent):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.left) + " " + str(self.right)


class Add(Operator):
	def getValue(self):
		return self.left.getValue() + self.right.getValue()


class Subtract(Operator):
	def getValue(self):
		return self.left.getValue() - self.right.getValue()


class Multiply(Operator):
	def getValue(self):
		return self.left.getValue() * self.right.getValue()


class Divide(Operator):
	def getValue(self):
		return self.left.getValue() / self.right.getValue()


class Modulo(Operator):
	def getValue(self):
		return self.left.getValue() % self.right.getValue()


class D(Operator):
	def __init__(self, left, right):
		super().__init__(left, right)
		self.diceBucket = DiceBucket(left, right)
		self.diceBucket.evaluate()

	def getValue(self):
		return self.diceBucket.getSum()

	def __str__(self):
		return " ".join(map(str, self.diceBucket.getRoll()))

