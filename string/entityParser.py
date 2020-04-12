class Solution3:
    def entityParser(self, text: str) -> str:
        dictionary = {"&quot;": "\"", "&apos;": "\'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        ans = text
        for html, target in dictionary.items():
            ans = ans.replace(html, target)
        return ans


k = Solution3()
print(k.entityParser(text="leetcode.com&frasl;problemset&frasl;all"))
