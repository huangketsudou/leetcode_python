class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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
        return len(nums)!=len(set(nums))
        
        
        
