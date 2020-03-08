from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def core(node,string):
            if not node:
                return string+'None,'
            string+=str(node.val)+','
            string=core(node.left,string)
            string=core(node.right,string)
            return string

        return core(root,'')


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data=data.split(',')
        def decore(d):
            if d[0]=='None':
                d.pop(0)
                return None
            n=d.pop(0)
            root=TreeNode(n)
            root.left=decore(d)
            root.right=decore(d)
            return root
        return decore(data)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        cur_nodes = [root]
        while cur_nodes:
            cur_res = []
            child_nodes = []
            for node in cur_nodes:
                if node:
                    cur_res.append(node.val)
                    child_nodes.append(node.left)
                    child_nodes.append(node.right)
                else:
                    cur_res.append(None)
            res.extend(cur_res)
            cur_nodes = child_nodes

        while res[-1] is None:
            res.pop()

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        length = len(data)
        if not length:
            return None

        root = TreeNode(data[0])
        parents = [root]
        childs = []
        i = 1
        while i < length:

            if childs:
                parents = childs
                childs = []

            for parent in parents:
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.left = node
                    childs.append(node)
                i += 1
                if i < length and data[i] is not None:
                    node = TreeNode(data[i])
                    parent.right = node
                    childs.append(node)
                i += 1

        return root


t1=TreeNode(1)
t2=TreeNode(2)
t1.left=t2

k=Codec()
a=k.serialize('')

b=k.deserialize(a)
