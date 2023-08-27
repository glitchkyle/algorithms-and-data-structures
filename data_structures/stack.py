from nodes import StackNode

class Stack(object):
    def __init__(self, nums):
        self.top = None
        for num in nums:
            self.push(num)
    
    def push(self, val):
        newNode = StackNode(val)
        # If stack exists
        if self.top is not None:
            newNode.bottom = self.top
            self.top = newNode
        else:
            self.top = newNode

    def pop(self):
        currentPtr = self.top
        popValue = self.top.data
        self.top = self.top.bottom
        del currentPtr
        return popValue

    def traverse(self):
        print("\nTraversing Stack")
        currentPtr = self.top
        while currentPtr is not None:
            print(currentPtr.data)
            currentPtr = currentPtr.bottom