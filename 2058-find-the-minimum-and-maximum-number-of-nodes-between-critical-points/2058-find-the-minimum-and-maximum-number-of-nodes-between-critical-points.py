# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [100000, -1]
        prev = 100000
        start = -1
        
        curr = head
        pv = curr.val
        i = 0
        while curr.next and curr.next.next:
            curr = curr.next
            i += 1
            if (pv < curr.val and curr.val > curr.next.val) or (pv > curr.val and curr.val < curr.next.val):
                print(i)
                if start == -1:
                    start = i
                else:
                    ans[0] = min(ans[0], i - prev)
                    ans[1] = max(ans[1], i - start)
                prev = i
            pv = curr.val
        if ans[0] == 100000:
            ans[0] = -1
        return ans