class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = deque()
        stack.append((0, 0))
        traveled = set()
        traveled.add((0, 0))
        ans = 1
        while stack:
            x, y = stack.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in traveled and self.legal(nx, ny) <= k:
                    traveled.add((nx, ny))
                    stack.append((nx, ny))
                    ans += 1
        return ans

    def legal(self, i, j):
        return sum([int(i) for i in str(i)]) + sum([int(i) for i in str(j)])


k=Solution()
print(k.movingCount(3,1,0))
