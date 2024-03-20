# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        for i in range(a-1):
            head = head.next
        keep = head
        for i in range(b-a+1):
            keep = keep.next
        head.next = list2
        while head.next:
            head = head.next
        head.next = keep.next
        return list1
        