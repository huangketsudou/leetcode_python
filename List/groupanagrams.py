from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from  collections import defaultdict
        hashmap=defaultdict(list)
        for i in strs:
            haxi=''.join(sorted(list(i)))
            hashmap[haxi].append(i)
        return list(hashmap.values())


class Solution2:
    def groupAnagrams(self,strs):
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()



k=Solution()
print(k.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

