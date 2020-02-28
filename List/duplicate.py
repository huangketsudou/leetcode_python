class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #绝对值之差小于k的定义为重复元素
        from collections import defaultdict
        contain=defaultdict(int=1)
        for i,v in enumerate(nums):
            if v in contain:
                if i-contain[v]<=k:
                    return True
            contain[v]=i
        return False
        
        
        
 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #只是元素重复
        return len(nums)!=len(set(nums))
        
        
        
#给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
#并且 i 和 j 之间的差的绝对值最大为 ķ。


class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        #线性搜索，超时
        for i in range(len(nums)):
            j=i+1
            while j<len(nums) and j<i+k+1:
                if abs(nums[i]-nums[j])<=t:
                    return True
                j+=1
        return False
    
    
class Solution4:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        #BST树方法，思路是维护一个大小为k的平衡二叉树，树中的元素索引最大不超过k，然后寻找与目标数值左右最接近的值找出其索引
        #方法思路没错，但是insert，delete操作太费时，慢
        from collections import deque
        import bisect
        n = len(nums)
        if n <= 1: return False
        m = min(n, k + 1)
        # 维护一个长度为 k + 1 队列
        queue = sorted(nums[:m])
        # 要删除数
        to_del = deque()
        to_del.extendleft(nums[:m])
        # 先判断首先 k + 1 队列是否存在满足条件的
        for i in range(1, m):
            if queue[i] - queue[i - 1] <= t:
                return True
        for i in range(m, n):
            # 移动队列
            queue.remove(to_del.pop())
            # 二分插入
            loc = bisect.bisect_left(queue, nums[i])
            queue.insert(loc, nums[i])
            # 判断它在队列中左右两边数是否小于等于t
            if (loc - 1 >= 0 and nums[i] - queue[loc - 1] <= t) or \
                    (loc + 1 <= k and queue[loc + 1] - nums[i] <= t):
                return True
            to_del.appendleft(nums[i])
        return False
    
    class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        #利用商作为桶的标记，关键是桶是如何实现的，k个桶，每个桶内仅有一个元素，寻找邻近的桶中的元素是否满足要求
        if t<0:return False
        w = t + 1
        def getId(num):
            return (num + 1) // w if num < 0 else num // w

        bucket = {}
        for i, v in enumerate(nums):
            m = getId(v)
            if m in bucket: return True
            if m - 1 in bucket and abs(bucket[m - 1] - v) < w:
                return True
            if m + 1 in bucket and abs(bucket[m + 1] - v) < w:
                return True
            bucket[m]=v
            if i>=k:
                del bucket[getId(nums[i-k])]
        return False


k = Solution3()
print(k.containsNearbyAlmostDuplicate([2,1],1,1))

