class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #把原来的节点的值赋给下一个节点，下一节点的值给这个节点，在跳过下一个节点
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val=node.next.val
        node.next=node.next.next
        
        
