class Solution3:
    def entityParser(self, text: str) -> str:
        dictionary = {"&quot;": "\"", "&apos;": "\'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        ans = text
        for html, target in dictionary.items():
            ans = ans.replace(html, target)
        return ans


k = Solution3()
print(k.entityParser(text="leetcode.com&frasl;problemset&frasl;all"))


class Solution:
    def entityParser(self, text: str) -> str:
        #题目里是有起始字符的&和终止字符；
        dic = {'&quot;': '\"', '&apos;': '\'', '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        n, right = len(text), 0
        curStr, res = "", ""
        while right < n:
            if right < n and text[right] != '&':
                res += text[right]; right += 1
            else:
                curStr = ""
                while right < n and text[right] != ';':
                    curStr += text[right]; right += 1
                curStr += ";"; right += 1
                if curStr in dic: res += dic[curStr]
                else: res += curStr
        return res
