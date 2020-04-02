class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table=[".-","-...","-.-.","-..",".","..-.","--.","....","..",
           ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
           "...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=set()
        for word in words:
            s=''
            for c in word:
                s+=table[ord(c)-ord('a')]
            ans.add(s)
        # seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
        #         for word in words}
        #
        # return len(seen)
        return len(ans)

