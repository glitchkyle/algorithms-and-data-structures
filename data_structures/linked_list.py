from nodes import ListNode

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