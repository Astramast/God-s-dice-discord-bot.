from abc import ABC, abstractmethod


class FormulaComponent(ABC):
        @abstractmethod
        def getValue(self):
                raise NotImplementedError


class Number(FormulaComponent):
        def __init__(self, value):
                self.value = value

        def getValue(self):
                return self.value

        def __str__(self):
                return str(self.value)

