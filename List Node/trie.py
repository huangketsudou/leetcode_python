from typing import List
import functools
import math
import itertools


# python简化字典树
class PythonTrie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        tree['#'] = '#'
        print(self.lookup)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if '#' in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = [None for i in range(26)]


# java字典树
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if node.next[ord(i) - ord('a')] is None:
                node.next[ord(i) - ord('a')] = TrieNode()
            node = node.next[ord(i) - ord('a')]
        node.isWord = True
        print(self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if node.next[ord(i) - ord('a')] is None:
                return False
            node=node.next[ord(i)-ord('a')]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for i in prefix:
            if node.next[ord(i)-ord('a')] is None:
                return False
            node=node.next[ord(i)-ord('a')]
        return True


k = Trie()
k.insert('blue')
k.insert('bully')
k.insert('apple')
