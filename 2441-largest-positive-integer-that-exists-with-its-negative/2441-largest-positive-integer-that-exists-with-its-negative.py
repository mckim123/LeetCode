class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for num in nums:
            if num < 0:
                continue
            if -num in s:
                ans = max(ans, num)
        return ans