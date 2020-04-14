class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        L1, L2 = l1, l2
        L1Node = []
        L2Node = []
        while L1 or L2:
            if L1:
                L1Node.append(L1)
                L1 = L1.next
            if L2:
                L2Node.append(L2)
                L2 = L2.next
        NewHead = None
        carry=0
        while L1Node or L2Node:
            l1Val=L1Node.pop().val if len(L1Node) else 0
            l2Val=L2Node.pop().val if len(L2Node) else 0
            carry,digit=divmod(l1Val+l2Val+carry,10)
            tmpNode=ListNode(digit)
            tmpNode.next=NewHead
            NewHead=tmpNode
        return NewHead
