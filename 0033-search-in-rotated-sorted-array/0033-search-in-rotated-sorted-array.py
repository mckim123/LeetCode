from bisect import bisect_left as bl
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = self.findMinIndex(nums)
        index = (bl(nums[m:] + nums[:m], target) + m) % len(nums)
        if nums[index] == target:
            return index
        return -1
        
        
    def findMinIndex(self, nums):
        n = len(nums)
        left = 0
        right = n-1
        while right - left > 1:
            left_num = nums[left]
            right_num = nums[right]
            if left_num < right_num:
                return nums.index(left_num)
            mid = (left + right) // 2
            mid_num = nums[mid]
            if mid_num > left_num:
                left = mid + 1
            else:
                right = mid
        return nums.index(min(nums[left], nums[right]))