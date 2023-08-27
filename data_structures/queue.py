from nodes import QueueNode

class Queue(object):
    def __init__(self, nodes):
        self.front = None
        self.back = None
        for node in nodes:
            self.enqueue(node)
    
    # Add node to queue
    def enqueue(self, val):
        newNode = QueueNode(val)
        # If queue is not empty
        if self.front is not None:
            self.back.next = newNode
            self.back = newNode
        else: 
            self.front = newNode
            self.back = newNode

    # Remove first node from queue
    def dequeue(self):
        if self.front is not None:
            current = self.front
            self.front = self.front.next
            return current
        
        return None

    # Search for node if node in queue
    def find(self, val):
        if self.front is not None:
            tempPtr = self.front
            while tempPtr is not None:
                if tempPtr.data == val:
                    return True
                tempPtr = tempPtr.next
        return False

    # Reverse queue
    def reverseQueue(self):
        if self.front is not None:
            prevPtr, nextPtr = None, None
            currentPtr = self.front

            while currentPtr is not None:
                nextPtr = currentPtr.next
                currentPtr.next = prevPtr
                prevPtr = currentPtr
                currentPtr = nextPtr

            self.front = prevPtr
    
    # Get front
    def peek(self):
        return self.front

    # Print Queue
    def traverse(self):
        print("\nTraversing Queue")
        if self.front is not None:
            tempPtr = self.front
            while(tempPtr is not None):
                print(tempPtr.data)
                tempPtr = tempPtr.next
