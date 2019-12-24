class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #原理为A+B=B+A,就算两者不相交，最终也会指向同样的None节点。
        h1,h2=headA,headB
        while h1!=h2:
            h1=h1.next if h1 else headB
            h2=h2.next if h2 else headA
        return h1


