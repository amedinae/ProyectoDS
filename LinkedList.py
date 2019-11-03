import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        nodes = []
        this = self.head
        while this:
            nodes.append(repr(this))
            this = this.next
        return '[' + ', '.join(nodes) + ']'
    
    def pushFront(self, key):
        if self.head:
            self.head = Node.Node(data = key, next = self.head)
        else :
            this = Node.Node(data = key)
            self.head = this
            self.tail = this
            
    def pushBack(self, key):
        if self.tail:
            this = Node.Node(data = key, next = None)
            self.tail.next = this
            self.tail = this
        else :
            this = Node.Node(data = key)
            self.head = this
            self.tail = this
    
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
        else:
            self.head = None
            self.tail = None
            
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
                        this = Node.Node(data = key)
                        prev.next = this
                        this.next = node.next

                    else:
                        return "Key {} don´t exist ".format(key)
                else:
                    self.pushFront(key)
                    
            else:
                return "Node don´t found"
        else:
            return "Linked list is empty" 
         
            
        
    def addAfter(self, node, key):
        if self.head:
            if self.find(node.data): # Después se puede quitar cuando todo funcione
                this = Node.Node(data = key)
                this.next = node.next
                node.next = this
            else:
                return "Node don´t found"
        else:
            return "Linked list is empty"

prueba = LinkedList()