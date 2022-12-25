# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        curr = node
        val = 0
        while l1 and l2:
            val += l1.val + l2.val
            curr.next = ListNode(val % 10)
            val //= 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            val += l1.val
            curr.next = ListNode(val % 10)
            val //= 10
            l1 = l1.next
            curr = curr.next
        while l2:
            val += l2.val
            curr.next = ListNode(val % 10)
            val //= 10
            l2 = l2.next
            curr = curr.next
        if val != 0:
            curr.next = ListNode(val)
        return node.next