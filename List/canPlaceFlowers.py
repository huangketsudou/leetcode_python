class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nums = [0] + flowerbed + [0]
        cnt = 0
        i = 1
        while i < len(flowerbed) + 1:
            if nums[i - 1] == 0 and nums[i] == 0 and nums[i + 1] == 0:
                cnt += 1
                # 可以种花，则需要间隔一个位置，所以+2
                i += 2
            else:
                i += 1

        return cnt >= n
