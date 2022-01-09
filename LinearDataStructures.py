from Nodes import QueueNode, StackNode, ListNode

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

class LinkedList(object):
    def __init__(self, nums):
        self.head = None
        self.end = None
        for num in nums:
            self.add(num) 
    
    def add(self, val):
        newNode = ListNode(val)
        # If list exists
        if self.head is not None:
            self.end.next = newNode
            self.end = newNode
        else:
            self.head = newNode
            self.end = self.head

    def delete(self, val):
        currentPtr = self.head
        previousPtr = None

        # Search for value in list
        while currentPtr is not None and currentPtr.data != val:
            previousPtr = currentPtr
            currentPtr = currentPtr.next

        # If value exists in list
        if currentPtr is not None:
            # If the found node is the head
            if currentPtr == self.head:
                self.head = self.head.next
            # If the found node is the rear
            elif currentPtr == self.end:
                previousPtr.next = None
            # If the found node is in between two nodes
            else:
                previousPtr.next = currentPtr.next

        del currentPtr

    def insert(self, newVal, val):
        newNode = ListNode(newVal)
        currentPtr = self.head
        prevPtr = None

        while currentPtr is not None:
            if currentPtr.data == val:
                if currentPtr == self.head:
                    self.head = newNode
                else:
                    prevPtr.next = newNode
                newNode.next = currentPtr
            prevPtr = currentPtr
            currentPtr = currentPtr.next

    def find(self, val):
        currentPtr = self.head

        while currentPtr is not None:
            if currentPtr.data == val:
                return currentPtr
            currentPtr = currentPtr.next

        return False
    
    # Binary sort
    def sort(self):
        currentPtr = self.head
        
        while currentPtr is not None:
            searchPtr = currentPtr.next
            while searchPtr is not None:
                if currentPtr.data > searchPtr.data:
                    tempNum = searchPtr.data
                    searchPtr.data = currentPtr.data
                    currentPtr.data = tempNum
                searchPtr = searchPtr.next
            currentPtr = currentPtr.next

    def reverse(self):
        previousPtr = None
        nextPtr = None
        currentPtr = self.head

        while currentPtr is not None:
            nextPtr = currentPtr.next
            currentPtr.next = previousPtr
            previousPtr = currentPtr
            currentPtr = nextPtr
        
        self.head = previousPtr

    def traverse(self):
        print("\nTraversing Linked List")
        currentPtr = self.head 
        while currentPtr is not None:
            print(currentPtr.data)
            currentPtr = currentPtr.next