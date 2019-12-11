# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        curr = dummyHead
        carried = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            curr.next = ListNode((a + b + carried) % 10)
            carried = (a + b + carried) // 10

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        curr.next = ListNode(1) if carried else None
        ret = dummyHead.next
        del dummyHead
        return ret