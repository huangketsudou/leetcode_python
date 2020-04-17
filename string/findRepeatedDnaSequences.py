from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, ans = set(), set()
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                ans.add(tmp)
            seen.add(tmp)
        return list(ans)


'''
Rabin-Karp算法思想
1.假设假设待匹配字符串的长度为M，目标字符串的长度为N（N>M）；
2.首先计算待匹配字符串的hash值，计算目标字符串前M个字符的hash值；
3.比较前面计算的两个hash值，比较次数N-M+1：
    3.1若hash值不相等，则继续计算目标字符串的下一个长度为M的字符子串的hash值
    3.2若hash值相同，则需要使用朴素算法再次判断是否为相同的字串；
原文链接：https://blog.csdn.net/chenhanzhun/article/details/39895077
伪代码：
Rabin_Karp_search(T, P, d,  q)
	n = T.length;
	m = P.length;
	h = d^(m-1)mod q; 
	p = 0;
	t = 0;
	for i =1 to m
	   p = (d*p+P[i]) mod q;
	   t = (d*t+T[i])mod q;
	for i = 0 to n-m   
		 if p==t
			 if P[1..m]==T[i+1..i+m]
			 print"Pattern occurs with shift"i
		 if i<n-m
			 t = d(t-T[i+1]h) + T[i+m+1]mod q
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n < L: return []
        a = 4
        aL = pow(a, L)
        to_int = {'A': 0, "C": 1, "G": 2, "T": 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        h = 0
        seen, ans = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                ans.add(s[start:start + L])
            seen.add(h)
        return list(ans)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L: return []
        to_int = {'A': 0, "C": 1, "G": 2, "T": 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        bitmask = 0
        seen, ans = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                bitmask <<= 2
                bitmask |= nums[start + L - 1]
                bitmask &= ~(3 << 2 * L)
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                ans.add(s[start:start + L])
            seen.add(bitmask)
        return list(ans)
