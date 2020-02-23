class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        #多种元素做一件事
        n = len(buildings)
        if n == 0: return []
        if n == 1:
            x_starts, x_end, y = buildings[0]
            return [[x_starts, y], [x_end, 0]]

        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])
        return self.merge_skyline(left_skyline, right_skyline)

    def merge_skyline(self, left, right):

        def update_output(x, y):
            if not output or output[-1][0] != x:
                #分出合并后的两天际线最后落在通过一各x坐标，但是最后的y值不同的情况
                output.append([x, y])
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):

            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y = left_y = right_y = 0
        output = []

        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # 用于处理剩余的部分天际线——left
        append_skyline(p_l, left, n_l, left_y, curr_y)
        # 用于处理剩余的部分天际线——right
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output

    
    
    import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #还是在抄作业
        #思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings:return []
        points = []
        heap = [[0, float('inf')]]
        res = [[0, 0]]

        #1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r)) #这里负号将最小堆，变成了最大堆
            points.append((r, h, 0)) #r的右端点为0

        #2.将端点从小到大排序
        points.sort() #如果当前点相等，则按照高度升序

        #3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:
            while l >= heap[0][1]: #出堆：保证当前堆顶为去除之前建筑物右端点的最大值。关键
                heapq.heappop(heap)
            if h < 0: #入堆：所有左端点都要入堆
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]: #关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
        return res[1:]
