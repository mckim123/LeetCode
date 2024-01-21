class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for num in nums:
            dp = [dp[1], max(dp[1], dp[0]+num)]
        return dp[1]