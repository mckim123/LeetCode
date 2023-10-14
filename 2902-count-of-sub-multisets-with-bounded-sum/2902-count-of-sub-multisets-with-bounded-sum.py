class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = int(1e9) + 7
        c = Counter(nums)
        zero_count = c[0]
        del c[0]

        # Initialize DP array to store counts of sums
        dp = [0] * (r+1)
        # Store counts assuming we could use the number infinitely
        infdp = [0] * (r+2)
        dp[0] = 1

        for num in c.keys():
            count = c[num]
            if num > r:
                continue

            for i in range(num):
                infdp[i] = dp[i]
            for i in range(num, r+1):
                infdp[i] = dp[i] + infdp[i-num]
            
            # Deduct counts where current number is used more than its occurrence in nums
            for i in range(1, r+1):
                dp[i] = (infdp[i] - infdp[max(-1, i - num * (count+ 1))]) % MOD
            

        return (sum(dp[l:]) * (1 + zero_count)) % MOD
