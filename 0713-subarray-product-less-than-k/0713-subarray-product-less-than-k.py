class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        l, r, ans = 0, 0, 0
        cur = nums[0]
        n = len(nums)
        while l < n:
            if cur < k or l > r:
                r += 1
                if r == n:
                    break
                cur *= nums[r]
            else:
                cur //= nums[l]
                ans += max(0, (r-l))
                l += 1
        return ans + ((n-l) * (n-l+1)) // 2
            