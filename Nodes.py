class Node(object):
    def __init__(self, data):
        self.data = data

class DoublyListNode(Node):
    def __init__(self, data, next=None, previous=None):
        super().__init__(data)
        self.previous = previous
        self.next = next

class ListNode(Node):
    def __init__(self, data, next=None):
        super().__init__(data)
        self.next = next

class StackNode(Node):
    def __init__(self, data, bottom=None):
        super().__init__(data)
        self.bottom = bottom

class QueueNode(Node):
    def __init__(self, data, next=None):
        super().__init__(data)
        self.next = next

class TreeNode(Node):
    def __init__(self, data, left=None, right=None):
        super().__init__(data)
        self.left = left
        self.right = right

    def hasLeftChild(self):
        return self.left is not None
    
    def hasRightChild(self):
        return self.right is not None

    def hasChildren(self):
        return (self.left is not None) and (self.right is not None)

class NodeOperations(object):
    # Swap values of two nodes
    def swap(self, nodeOne, nodeTwo):
        tempData = nodeOne.data
        nodeOne.data = nodeTwo.data
        nodeTwo.data = tempData
