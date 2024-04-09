class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m = tickets[k]
        ans = 0
        for i, t in enumerate(tickets):
            ans += min(m-int(i>k), t)
        return ans