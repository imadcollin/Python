class Stack: 
    def __init__(self):
        self.stack = []
        
    def add(self, data): 
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            print("Element Already Exist")
            return False
    
    def peek(self): 
        return self.stack.pop()
    
    def stackSize(self):
        return len(self.stack)
    
    def pritnStack(self): 
        for i in self.stack:
            print('elem -> ', i)

    
AStack =Stack()
AStack.add('A') 
AStack.add('B')
AStack.pritnStack() 

print('############ Peek #######33')
AStack.peek()
print(AStack.stackSize())
AStack.pritnStack()