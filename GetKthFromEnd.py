# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getKthFromEnd( head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    former_node = latter_node = head
    if head == None:
        return None
    while former_node!=None:
        if k>0:
            k-=1
        else:
            latter_node = latter_node.next
        former_node = former_node.next
    return latter_node


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
ret = getKthFromEnd(head,2)
print(ret.val)
