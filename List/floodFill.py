class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n,m=len(image),len(image[0])
        point=(sr,sc)
        target=image[sr][sc]
        if target==newColor: return image
        image[sr][sc]=newColor
        stack=deque()
        stack.append(point)
        direction=[(-1,0),(1,0),(0,1),(0,-1)]
        while stack:
            x,y=stack.popleft()
            for dx,dy in direction:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and image[nx][ny]==target:
                    image[nx][ny]=newColor
                    stack.append((nx,ny))
        return image
