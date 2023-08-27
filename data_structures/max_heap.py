from tree import Tree
from nodes import NodeOperations

class MaxHeap(Tree):
    def insert(self, val):
        super().insert(val)

    def delete(self, val):
        super().delete(val)

    def heapifyMax(self, node):
        if node is not None:
            self.heapifyMax(node.left)
            self.heapifyMax(node.right)

            if node.hasChildren():
                largestChild = max(node.left.data, node.right.data)
                if largestChild > node.data:
                    if largestChild == node.left.data:
                        NodeOperations.swap(node, node.left)
                        self.heapifyMax(node.left)
                    elif largestChild == node.right.data:
                        NodeOperations.swap(node, node.right)
                        self.heapifyMax(node.right)
            elif node.hasLeftChild():
                if node.data < node.left.data:
                    NodeOperations.swap(node, node.left)
                    self.heapifyMax(node.left)
            elif node.hasRightChild():
                if node.data < node.right.data:
                    NodeOperations.swap(node, node.right)
                    self.heapifyMax(node.right)
