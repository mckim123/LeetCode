class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        curr = 0
        for i in range(n):
            nums[i] ^= curr
            if nums[i] == 0:
                if i >= n-k+1:
                    return -1
                ans += 1
                curr ^= 1
            if i >= k-1:
                curr ^= not nums[i-k+1]
        return ans