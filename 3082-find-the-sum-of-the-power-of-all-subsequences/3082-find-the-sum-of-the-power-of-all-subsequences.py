class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = [[0] * (n+1) for _ in range(k+1)]
        c[0][0] = 1
        MOD = 10 ** 9 + 7

        for num in nums:
            if num > k:
                continue
            for m in range(n, 0, -1):
                for j in range(k, num-1, -1):
                    c[j][m] = (c[j][m]+c[j-num][m-1])% MOD

        res = c[k]
        ans = 0
        for i in range(len(nums)+1):
            ans <<= 1
            ans += res[i]
            ans %= MOD
        return ans
