class MyCircularQueue:

    def __init__(self, k: int):
        self.myArray = [None]*k
        self.size = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.size
        self.myArray[self.tail] = value
        return True
            

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1) % self.size
        return True
        
        
    def Front(self) -> int:
        return self.myArray[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.myArray[self.tail] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        return True if self.head == -1 else False

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head