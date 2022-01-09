from Nodes import TreeNode, NodeOperations

op = NodeOperations()

class Tree(object):
    def __init__(self, nums):
        self.root = None
        for num in nums:
            self.insert(num)

    def insert(self, val):
        newNode = TreeNode(val)
        if self.root is not None:
            nodeQueue = [self.root]
            while len(nodeQueue) > 0:
                currentSearchNode = nodeQueue[0]
                nodeQueue.remove(currentSearchNode)

                if currentSearchNode.hasLeftChild():
                    nodeQueue.append(currentSearchNode.left)
                else:
                    currentSearchNode.left = newNode
                    break
                
                if currentSearchNode.hasRightChild():
                    nodeQueue.append(currentSearchNode.right)
                else:
                    currentSearchNode.right = newNode
                    break
        else:
            self.root = newNode
    
    def delete(self, val):
        if self.root is not None:

            # Search for node 
            deleteNode = self.findNode(val)

            if deleteNode is None:
                return

            # Search for parent of delete node for deletion
            parentNode = self.findParent(val, self.root)

            # Find last node
            lastNode = self.findLastNode(self.root)

            # Swap (last node will contain delete val)
            op.swap(lastNode, deleteNode)

            # Delete
            if parentNode.left is lastNode:
                parentNode.left = None
            elif parentNode.right is lastNode:
                parentNode.right = None
    
    def findNode(self, val):
        nodeList = []
        nodeQueue = [self.root]
        while len(nodeQueue) > 0:
            currentSearchNode = nodeQueue[0]
            nodeQueue.remove(currentSearchNode)

            if currentSearchNode.hasLeftChild():
                nodeQueue.append(currentSearchNode.left)
                nodeList.append(currentSearchNode.left)

            if currentSearchNode.hasRightChild():
                nodeQueue.append(currentSearchNode.right)
                nodeList.append(currentSearchNode.right)
        
        for i in range(len(nodeList)):
            if nodeList[i].data == val:
                return nodeList[i]
        
        return None
    
    def findLastNode(self, node):
        if node.hasRightChild():
            return self.findLastNode(node.right)
        elif node.hasLeftChild():
            return self.findLastNode(node.left)
        return node
        
    def peek(self):
        return self.root

    def traversePreOrder(self, node):
        if node is not None:
            print(node.data)
            self.traversePreOrder(node.left)
            self.traversePreOrder(node.right)
            
    def traversePostOrder(self, node):
        if node is not None:
            self.traversePostOrder(node.left)
            self.traversePostOrder(node.right)
            print(node.data)

    def traverseInOrder(self, node):
        if node is not None:
            self.traverseInOrder(node.left)
            print(node.data)
            self.traverseInOrder(node.right)

    def invert(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self.invert(node.left)
            self.invert(node.right)

    def findParent(self, val, currentNode, parentNode=None):
        if currentNode is not None:
            if currentNode.data == val:
                if currentNode == self.root:
                    return self.root
                else:
                    return parentNode
            else:
                leftSideSearch = self.findParent(val, currentNode.left, currentNode)
                rightSideSearch = self.findParent(val, currentNode.right, currentNode)
                if leftSideSearch is not None:
                    return leftSideSearch
                elif rightSideSearch is not None:
                    return rightSideSearch
        
        return None

class Heap(Tree):
    def insert(self, val):
        super().insert(val)
        #self.heapifyMax(self.root)
        #self.heapifyMin(self.root)
    
    def delete(self, val):
        super().delete(val)
        #self.heapifyMax(self.root)
        #self.heapifyMin(self.root)

    # Sort until largest is on top
    def heapifyMax(self, node):
        if node is not None:
            self.heapifyMax(node.left)
            self.heapifyMax(node.right)

            if node.hasChildren():
                largestChild = max(node.left.data, node.right.data)
                if largestChild > node.data:
                    if largestChild == node.left.data:
                        op.swap(node, node.left)
                        self.heapifyMax(node.left)
                    elif largestChild == node.right.data:
                        op.swap(node, node.right)
                        self.heapifyMax(node.right)
            elif node.hasLeftChild():
                if node.data < node.left.data:
                    op.swap(node, node.left)
                    self.heapifyMax(node.left)
            elif node.hasRightChild():
                if node.data < node.right.data:
                    op.swap(node, node.right)
                    self.heapifyMax(node.right)

    # Sort until smallest is on top
    def heapifyMin(self, node):
        if node is not None:
            self.heapifyMin(node.left)
            self.heapifyMin(node.right)

            if node.hasLeftChild() and node.hasRightChild():
                smallest = min(node.left.data, node.right.data)
                if smallest < node.data:
                    if smallest == node.left.data:
                        op.swap(node, node.left)
                        self.heapifyMin(node.left)
                    elif smallest == node.right.data:
                        op.swap(node, node.right)
                        self.heapifyMin(node.right)
            elif node.hasLeftChild():
                if node.data > node.left.data:
                    op.swap(node, node.left)
                    self.heapifyMin(node.left)
            elif node.hasRightChild():
                if node.data > node.right.data:
                    op.swap(node, node.right)
                    self.heapifyMin(node.right)