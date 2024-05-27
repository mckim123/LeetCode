class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = n-1
        x = n
        curr = 0
        while x >= 0:
            while i >= 0 and nums[i] >= x:
                i -= 1
                curr += 1
            if x == curr:
                return curr
            x -= 1
        return x