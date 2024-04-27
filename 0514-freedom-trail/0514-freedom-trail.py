class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        INF = 10 ** 6
        dp = [min(i, n-i) for i in range(n)]
        idxs = defaultdict(list)
        
        for i, ch in enumerate(ring):
            idxs[ch].append(i)
        
        for ch in key:
            dp1 = [INF] * n
            indices = idxs[ch]
            
            for i in indices:
                for j, val in enumerate(dp):
                    d = abs(i-j)
                    dp1[i] =  min(dp1[i], val + min(d, n-d))
            dp = dp1
        
        return min(dp) + len(key)