from tree import Tree
from nodes import NodeOperations

class MinHeap(Tree):
    def insert(self, val):
        super().insert(val)

    def delete(self, val):
        super().delete(val)

    def heapifyMin(self, node):
        if node is not None:
            self.heapifyMin(node.left)
            self.heapifyMin(node.right)

            if node.hasLeftChild() and node.hasRightChild():
                smallest = min(node.left.data, node.right.data)
                if smallest < node.data:
                    if smallest == node.left.data:
                        NodeOperations.swap(node, node.left)
                        self.heapifyMin(node.left)
                    elif smallest == node.right.data:
                        NodeOperations.swap(node, node.right)
                        self.heapifyMin(node.right)
            elif node.hasLeftChild():
                if node.data > node.left.data:
                    NodeOperations.swap(node, node.left)
                    self.heapifyMin(node.left)
            elif node.hasRightChild():
                if node.data > node.right.data:
                    NodeOperations.swap(node, node.right)
                    self.heapifyMin(node.right)
