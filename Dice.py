from random import randint


class Dice:
	def __init__(self, faces):
		self.faces = faces

	def roll(self):
		return randint(1, self.faces)


class DiceRoller:
	def __init__(self, dice):
		self.dice = dice

	def roll(self, times):
		return [self.dice.roll() for _ in range(times)]


class DiceBucket:
	def __init__(self, diceAmount, faces):
		self.diceRoller = DiceRoller(Dice(faces))
		self.diceAmount = diceAmount
		self.roll = None

	def evaluate(self):
		if self.roll is not None:
			raise Exception("Roll already done")
		self.roll = self.diceRoller.roll(self.diceAmount)

	def getRoll(self):
		if self.roll is None:
			raise Exception("Roll not yet done")
		return self.roll

	def getSum(self):
		return sum(self.getRoll())

