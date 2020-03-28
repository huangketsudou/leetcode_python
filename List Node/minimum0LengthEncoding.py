#字典树

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie={'#':{}}
        for word in words:
            tree=trie['#']
            for i in word[::-1]:
                if i not in tree:
                    tree[i]={}
                tree=tree[i]
        stack=deque()
        stack.append((trie['#'],1))
        res=0
        while stack:
            node,depth=stack.popleft()
            if not node:
                res+=depth
                continue
            for n in node.keys():
                stack.append((node[n],depth+1))
        return res


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                #如果某个单词是另一个单词的后缀，就把他删了
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)



k=Solution()
words = ["time", "me", "bell"]
print(k.minimumLengthEncoding(["time", "atime", "btime"]))
