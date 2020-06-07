from collections import deque


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.history.append(homepage)
        self.size = 1
        self.currentidx = 0

    def visit(self, url: str) -> None:
        while self.currentidx + 1 != self.size:
            self.history.pop()
            self.size -= 1
        self.history.append(url)
        self.size += 1
        self.currentidx += 1

    def back(self, steps: int) -> str:
        tmp = max(0, self.currentidx - steps)
        self.currentidx = tmp
        return self.history[self.currentidx]

    def forward(self, steps: int) -> str:
        tmp = min(self.size - 1, self.currentidx + steps)
        self.currentidx = tmp
        return self.history[self.currentidx]
