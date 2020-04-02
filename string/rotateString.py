class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n, m = len(A), len(B)
        if n != m: return False
        if n == 0: return True
        f = self.compute_KMP(B)
        newA = A + A
        i = 0
        k = 0
        while i < n:
            while newA[i] == B[k]:
                k += 1
                i += 1
                if i == n:
                    return True
            if k != 0:
                k = f[k - 1]
            else:
                i += 1
        return False

    def compute_KMP(self, S):
        n = len(S)
        fail = [0] * n
        i = 1
        k = 0
        while i < n:
            if S[i] == S[k]:
                fail[i] = k + 1
                i += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                i = i + 1
        return fail
        
        
        
        
        
       
       
       
class Solution(object):
    def rotateString(self, A, B):
        MOD = 10**9 + 7
        P = 113
        Pinv = pow(P, MOD-2, MOD)

        hb = 0
        power = 1
        for x in B:
            code = ord(x) - 96
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in A:
            code = ord(x) - 96
            ha = (ha + power * code) % MOD
            power = power * P % MOD

        if ha == hb and A == B: return True
        for i, x in enumerate(A):
            code = ord(x) - 96
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i+1:] + A[:i+1] == B:
                return True
        return False
明出处。
