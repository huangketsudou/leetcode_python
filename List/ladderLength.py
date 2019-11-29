from typing import List


class Solution:
    #广度优先搜索找最短路径
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:return 0
        from collections import defaultdict
        L=len(beginWord)
        all_comb_dict=defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_comb_dict[word[:i]+'*'+word[i+1:]].append(word)
        queue=[(beginWord,1)]
        visited={beginWord:True}
        while queue:
            currentword,level=queue.pop(0)
            for i in range(L):
                intermediate_word=currentword[:i]+'*'+currentword[i+1:]
                for word in all_comb_dict[intermediate_word]:
                    if word==endWord:return level+1
                    if word not in visited:
                        visited[word]=True
                        queue.append((word,level+1))
                all_comb_dict[intermediate_word]=[]

        return 0


class Solution2:
    #双向广度优先搜索找最短路径
    def __init__(self):
        from collections import defaultdict
        self.length=0
        self.all_comb_dict=defaultdict(list)


    def visitWordNode(self,queue,visited,other_visited):
        currentWord,level=queue.pop(0)
        for i in range(self.length):
            intermediate_word=currentWord[:i]+'*'+currentWord[i+1:]
            for word in self.all_comb_dict[intermediate_word]:
                if word in other_visited:
                    return level+other_visited[word]
                if word not in visited:
                    visited[word]=level+1
                    queue.append((word,level+1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:return 0
        self.length=len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.all_comb_dict[word[:i]+'*'+word[i+1:]].append(word)
        queue_begin=[(beginWord,1)]
        queue_end=[(endWord,1)]
        visited_begin={beginWord:True}
        visited_end={endWord:True}
        while queue_begin and queue_end:
            ans=self.visitWordNode(queue_begin,visited_begin,visited_end)
            if ans:
                return ans
            ans=self.visitWordNode(queue_end,visited_end,visited_begin)
            if ans:return ans
        return 0


    
    
 class Solution:
    # 广度优先搜索找最短路径
    #给出相应的最短路径
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not endWord or not beginWord or not wordList: return []
        from collections import defaultdict
        L = len(beginWord)
        all_comb_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_comb_dict[word[:i] + '*' + word[i + 1:]].append(word)
        queue = [(beginWord, [beginWord],1)]
        answer=[]
        visited={beginWord:1}
        firstfound=True
        minlevel=0
        while queue:
            currentword, path ,level= queue.pop(0)
            for i in range(L):
                intermediate_word = currentword[:i] + '*' + currentword[i + 1:]
                for word in all_comb_dict[intermediate_word]:
                    if word==endWord and word not in path:
                        if firstfound:
                            answer.append(path+[word])
                            firstfound=False
                            minlevel=level+1
                        else:
                            if level+1>minlevel:
                                return answer
                            else:
                                answer.append(path+[word])
                        continue
                    if word not in visited or visited[word]>=level+1:
                        visited[word]=1+level
                        queue.append((word,path+[word],level+1))

        return answer

k=Solution2()
print(k.ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"]))
