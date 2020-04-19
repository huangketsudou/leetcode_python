from collections import Counter
from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = [0 for i in range(5)]

        idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        #croak为一句叫声，叫完放走，没叫完，计数加一
        minNum = -1

        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i] in idx:
                t = idx[croakOfFrogs[i]]
                if t == 0:
                    cnt[0] += 1
                else:
                    if cnt[t - 1] > 0:
                        cnt[t - 1] -= 1
                        cnt[t] += 1
                    else:
                        return -1

                minNum = max(minNum, sum(cnt[:-1]))
            else:
                return -1

        if sum(cnt[:-1]) > 0:
            return -1

        return minNum


k=Solution()
print(k.minNumberOfFrogs('croak'))