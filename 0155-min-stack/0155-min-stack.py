class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # This will store tuples of (current_value, current_min)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1][1]:
            self.min_stack.append((val, val))
        else:
            self.min_stack.append((val, self.min_stack[-1][1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][1]
