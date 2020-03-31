class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=len)
        c=defaultdict(int)
        for i in licensePlate:
            if 97<=ord(i)<=122 or 65<=ord(i)<=90:
                c[i.lower()]+=1

        for word in words:
            if self.compare(c,word):
                return word
        return ''

    def compare(self,pattern,word):
        s=Counter(word)
        for k,v in pattern.items():
            if k not in s or s[k]<v:
                return False
        return True
