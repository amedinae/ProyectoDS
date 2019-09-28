class Stack(LinkedList):
    def push(self, key):
        self.pushBack(key)
        
    def top(self):
        self.topBack()
        
    def pop(self):
        this = self.topBack()
        self.popBack()
        return this
        
    def empty(self):
        self.empty()