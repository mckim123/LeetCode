class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        m, M = a[0][-1], a[0][0]
        ans = 0
        
        for b in a:
            ans = max(ans, M-b[0], b[-1]-m)
            m = min(m, b[0])
            M = max(M, b[-1])
        
        return ans