import LinkedList

class Queue(LinkedList.LinkedList):
    def enqueue(self, key):
        self.pushBack(key)
        
    def dequeue(self):
        this = self.topFront()
        self.popFront()
        return this
    
    def empty(self):
        self.empty()