class MinStack:

    def __init__(self):
        self.stack = []
        self.minm = 99999999999

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minm:
            self.minm=val

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.stack)==0:
            self.minm = 99999999999
        else:    
            self.minm=min(self.stack)    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minm