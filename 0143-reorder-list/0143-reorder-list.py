# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        queue = deque()
        ans = head
        t = head
        t = t.next
        while t:
            queue.append(t)
            t = t.next
        
        ans.next = None
        right = True
        while queue:
            if right:
                curr = queue.pop()
            else:
                curr = queue.popleft()
            right = not right
            ans.next = curr
            ans = ans.next
            ans.next = None
        return head
            