from random import choice


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.list = []
        self.store(head)
        self.size=len(self.list)


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        idx=choice(range(self.size))
        return self.list[idx]

    def store(self, head):
        while head:
            self.list.append(head.val)
            head = head.next


import random



'''
https://leetcode-cn.com/problems/linked-list-random-node/solution/xu-shui-chi-chou-yang-suan-fa-by-jackwener/
蓄水池抽样算法
题目问题：当内存无法加载全部数据时如何随机选择K个数字
当k=1时，每次只保留一个数，以1/i的概率保留该数，（i-1）/i的概率保留原来的数，对于1-10的数组
遇到1时，概率为1，保留该数,遇到2，概率为1/2，1和2各1/2的概率保留，
遇到3时，3被保留的概率为1/3，对于上一个留下来的数，这一轮被保留的概率为2/3，而上上轮中，1被保留的概率为1/2，
综合概率为1/3
当k=m时，假设数据流中含有N个数据，要保证每条数据被抽到的概率相同，那么每个数据被抽取的概率为k/N
对于前k个数n1,n2,n3,...nk,都保留下来，p(n1)=p(n2)=...=p(nk)=1
对于第k+1个数，以k/(k+1)的概率保留他，那么对于前k个数nr（r=[1,k]）被保留的概率可以表示为
p(nr被保留)=p(上一轮nr被保留)*p(nk+1被丢弃)+p(nk+1被保留)*p(nr未被替换)
p(nr)=1/(k+1)+k/(k+1)*(k-1)/k=k/(k+1)
对于k+2个数，以k+2的概率保留他，那么前k+1个被保留下来的数中的nr被保留的概率为
p(nr)=k/(k+1)*2/(k+2)+k/(k+1)*(k-1)/(k+2)=2/(k+2)
......
对于第i个数ni，以k/i的概率保留，则前i个数被保留的概率为：
p(nr)=k/(i-1)*(i-k)/i+k/(i-1)*(k-1)/i=k/i
这里最后的(k-1)/i是被保留且不被替换的概率，可以这样理解，对于前i-1个数，其被保留的概率是k/(i-1),从被保留的k个数
中选一个被替换，概率为1/k，所以这个数不被替换的概率为1-1/k，所以综合概率为(k-1)/(i-1)

'''

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1, count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve

