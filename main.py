from LinearDataStructures import *
from NonLinearDataStructures import *
from Algorithms import *

searcher = SearchingAlgorithm()
sorter = SortingAlgorithm()

if __name__ == '__main__':
    print("Test")
    tree = Tree([1, 2, 3, 4, 5])
    tree.traversePreOrder(tree.root)
    tree.delete(2)
    print("\n")
    tree.traversePreOrder(tree.root)