class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while right - left > 1:
            left_num = nums[left]
            right_num = nums[right]
            if left_num < right_num:
                return left_num
            mid = (left + right) // 2
            mid_num = nums[mid]
            if mid_num > left_num:
                left = mid + 1
            else:
                right = mid
        return min(nums[left], nums[right])