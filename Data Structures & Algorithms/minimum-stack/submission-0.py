class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # pushes the element on to the stack
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        # removes the element on the top of the stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # gets the top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        #  retrieves the minimum element in the stack
        return self.min_stack[-1]
