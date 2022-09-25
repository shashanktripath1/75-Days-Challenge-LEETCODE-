class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.data = [-1] * k
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.rear = (self.rear + 1) % self.k
        self.data[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.k
        if self.front - self.rear == 1 or (self.front == 0 and self.rear == self.k-1):
            self.front = 0
            self.rear = -1
        return True
    
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.rear]
    
    def isEmpty(self) -> bool:
        return self.rear == -1

    def isFull(self) -> bool:
        return (self.rear == self.k-1 and self.front == 0) or (self.rear != -1 and self.front - self.rear == 1)
