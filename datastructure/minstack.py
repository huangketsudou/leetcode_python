class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack)==0 or x<self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack)>0:
            return self.minstack[-1]