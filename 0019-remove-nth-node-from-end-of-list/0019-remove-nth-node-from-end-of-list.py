# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy
        n1 = 0
        while curr.next:
            curr = curr.next
            n1 += 1
        
        def remove(head, m):
            if m:
                head.next = remove(head.next, m-1)
            else:
                head.next = head.next.next
            return head
        remove(dummy, n1-n)
        return dummy.next