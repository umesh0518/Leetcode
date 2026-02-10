class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #we get the last elelment if it exit else value and then choose the min between them
        val = min( val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        #also need to pop the mins tack as they are equal length
        # minstak might store duplicates but min value is always at last.
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()