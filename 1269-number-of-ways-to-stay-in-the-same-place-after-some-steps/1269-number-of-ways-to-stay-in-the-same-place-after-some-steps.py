class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9) + 7
        arrLen = min(steps // 2 + 2, arrLen)
        
        dp = [0] * arrLen
        dp[0] = 1
        next_dp = [0] * arrLen
        next_dp[0] = 1
        
        for i in range(steps):
            for j in range(min(i+2, arrLen)):
                if j-1 >= 0:
                    next_dp[j] += dp[j-1]
                if j+1 < arrLen:
                    next_dp[j] += dp[j+1]
                next_dp[j] %= MOD
            dp = next_dp.copy()
        
        return dp[0]
