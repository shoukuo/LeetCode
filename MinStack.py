class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minst = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minst) == 0 or x < self.minst[-1][0]:
            self.minst.append([x, 1])
        else:
            self.minst[-1][1] += 1
        return x

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.minst[-1][1] -= 1
        if self.minst[-1][1] == 0:
            self.minst.pop()
            
    # @return an integer
    def top(self):
        return self.stack[-1]
    
    # @return an integer
    def getMin(self):
        return self.minst[-1][0]
        
def printst(st):
    print st.stack
    print st.minst
    
def printTopMin(st):
    print st.top()
    print st.getMin()
