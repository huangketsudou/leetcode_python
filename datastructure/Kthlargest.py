class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.storage = []
        self.kmax = []
        self.maxlength = k
        self.curlength = 0
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.storage.append(val)
        if self.curlength < self.maxlength:
            heappush(self.kmax, val)
            self.curlength += 1
        else:
            if val>self.kmax[0]:
                heappop(self.kmax)
                heappush(self.kmax,val)
        return self.kmax[0]
