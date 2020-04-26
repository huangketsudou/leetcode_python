from typing import List



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None



    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        que , curs = [] , [] # curs存K个链表滑动的头指针
        #用一个curs存头指针，heapq可以对元组进行比较，当他们的值相同时，index小的先出来
        for index, node in enumerate(lists):
                if node!=None:
                    heapq.heappush(que ,(node.val, index))
                curs.append(node)

        dummy_node = ListNode(-1)
        cur = dummy_node
        while que:
            val, index =  heapq.heappop(que)
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] != None:
                heapq.heappush(que, (lists[index].val, index))
        return dummy_node.next


