class Solution:
    def numSquares(self, n: int) -> int:
        m = int(n ** (1/2))
        if m ** 2 == n or (m+1) ** 2 == n:
            return 1
        
        squares = [i ** 2 for i in range(1, m+1)]
        
        dp = [n] * (n+1)
        dp[0] = 1
        
        for j in range(1, n):
            j1 = int(j ** (1/2))
            if j == j1 ** 2:
                dp[j] = 1
            for k in range(1, j1+1):
                k1 = k ** 2
                if j + k1 <= n and dp[j+k1] > dp[j] + 1:
                    dp[j+k1] = dp[j]+1
        return dp[-1]
                
                