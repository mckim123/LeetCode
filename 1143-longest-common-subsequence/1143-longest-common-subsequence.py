class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        
        for i in range(n1):
            ch1 = text1[i]
            for j in range(n2):
                if ch1 == text2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                dp[i][j+1] = max(dp[i][j+1], dp[i][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        m1 = max(dp[-1])
        m2 = max(dp[i][-1] for i in range(n1+1))
        return max(m1, m2)