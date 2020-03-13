class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first='qwertyuiop'
        second='asdfghjkl'
        third='zxcvbnm'
        result=[]
        for word in words:
            if self.match(word,first):
                result.append(word)
                continue
            if self.match(word,second):
                result.append(word)
                continue
            if self.match(word,third):
                result.append(word)
        return result

    def match(self,word,pattern):
        tmp=word.lower()
        for i in tmp:
            if i not in pattern:
                return False
        return True


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(filter(lambda word: any(set(word.lower()).issubset(line) for line in [set('asdfghjkl'),set('qwertyuiop'),set('zxcvbnm')]),words))




k=Solution()
print(k.findWords(["Hello", "Alaska", "Dad", "Peace"]))
