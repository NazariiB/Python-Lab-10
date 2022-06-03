from Lab_10 import Resistor


class Node:
    def __init__(self, resistor: Resistor):
        self.resistor = resistor
        self.right = None
        self.left = None
