from Lab_10.BinaryTree import BinaryTree
from Lab_10.Resistor import Resistor

if __name__ == "__main__":
    print("\n\nCreate and add Resistors to tree\n")
    tree = BinaryTree()
    tree.add_resistor(Resistor("d", 100, 100, 80))
    tree.add_resistor(Resistor("b", 100, 100, 80))
    tree.add_resistor(Resistor("c", 90, 1, 8))
    tree.add_resistor(Resistor("a", 80, 1, 9))
    tree.add_resistor(Resistor("b", 110, 1, 1))
    tree.add_resistor(Resistor("o", 10, 1, 6))
    tree.add_resistor(Resistor("f", 70, 1, 6))
    tree.print_tree()
    print("___________________________________\nDelete all Resistor with precision = 6 \n")
    tree.delete_nodes_with_precision(6)
    tree.print_tree()
    print("___________________________________\nPrint all Resistor with nominal = 100 \n")
    tree.print_nodes_with_nominal(100)
    print("___________________________________\nDelete tree ")
    tree.delete_tree()
    tree.print_tree()