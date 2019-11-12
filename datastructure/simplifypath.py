from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


k=Solution()
b="/a//b////c/d//././/.."
print(k.simplifyPath(b))
