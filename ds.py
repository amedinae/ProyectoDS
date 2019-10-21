class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _iter_(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __repr__(self):
        nodes = []
        this = self.head
        while this:
            nodes.append(repr(this))
            this = this.next
        return '[' + ', '.join(nodes) + ']'
    
    def pushFront(self, key):
        if self.head:
            self.head = Node(data = key, next = self.head)
        else :
            this = Node(data = key)
            self.head = this
            self.tail = this
        self.size += 1
            
    def pushBack(self, key):
        if self.tail:
            this = Node(data = key, next = None)
            self.tail.next = this
            self.tail = this
        else :
            this = Node(data = key)
            self.head = this
            self.tail = this
        self.size += 1
    
    def topFront(self):
        if self.head:
            return self.head
        else:
            return "Linked list is empty"
    
    def topBack(self):
        if self.tail:
            return self.tail
        else:
            return "Linked list is empty"
        
    def popFront(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1
        else:
            return "Linked list is empty"
        
    def popBack(self):
        if not self.head:
            return "Linked list is empty"
        elif self.head != self.tail:
            this = self.head
            while this.next != self.tail:
                this = this.next
            this.next = None
            self.tail = this
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            self.size -= 1
            
    def find(self, key):
        if self.head:
            this = self.head
            while this.data != key and this.next:
                this = this.next
            if this.data == key:
                return True
            else:
                return False
        else:
            return "Linked list is empty"
        
    def erase(self, key):
        if self.head:
            this = self.head
            prev = None
            while this.data != key and this.next:
                prev = this
                this = this.next
            if this.data == key:
                prev.next = this.next
                this = None
            else:
                return "Key {} don´t exist ".format(key)
        else:
            return "Linked list is empty"
    
    def empty(self):
        if self.head:
            return True
        else:
            return False
        
    def addBefore(self, node, key):
        if self.head:
            if self.find(node.data):
                this = self.head
                prev = None
                
                if this != self.head:
                
                    while this != node and this.next:
                        prev = this
                        this = this.next

                    if this == node:
                        this = Node(data = key)
                        prev.next = this
                        this.next = node.next
                        self.size += 1

                    else:
                        return "Key {} don´t exist ".format(key)
                else:
                    self.pushFront(key)
                    self.size += 1
                    
            else:
                return "Node don´t found"
        else:
            return "Linked list is empty" 
         
            
        
    def addAfter(self, node, key):
        if self.head:
            if self.find(node.data): # Después se puede quitar cuando todo funcione
                this = Node(data = key)
                this.next = node.next
                node.next = this
                self.size += 1
            else:
                return "Node don´t found"
        else:
            return "Linked list is empty"


class Stack(LinkedList):
    def push(self, key):
        self.pushFront(key)
        
    def top(self):
        self.topFront()
        
    def pop(self):
        this = self.topFront()
        self.popFront()
        return this
        
    def empty(self):
        self.empty()


class Queue(LinkedList):
    def enqueue(self, key):
        self.pushBack(key)
        
    def dequeue(self):
        this = self.topFront()
        self.popFront()
        return this

    def peek(self):
        return self.topFront()
    
    def empty(self):
        self.empty()
