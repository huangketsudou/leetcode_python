class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        n = len(S)
        if n < K: return S
        result = ''
        k = 0
        for i in range(n - 1, -1, -1):
            f = ord(S[i])
            if 48 <= f <= 57 or 97 <= f <= 122 or 65 <= f <= 90:
                if k == K:
                    result = S[i].upper() + '-' + result
                    k = 1
                else:
                    result = S[i].upper() + result
                    k += 1

        return result


class Solution2:
    def licenseKeyFormatting(self, S, K):
        new_S = "".join(S.split("-")).upper()
        if len(new_S) % K:
            new_S = new_S.rjust(K - len(new_S) % K + len(new_S))

        return "-".join(new_S[i:i + K] for i in range(0, len(new_S), K)).lstrip()


k = Solution2()
print(k.licenseKeyFormatting(S="2-5g-3-J", K=2))


