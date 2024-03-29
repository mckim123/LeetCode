class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefix = 0
        m = 0
        answer = -10**5
        for num in nums:
            prefix += num
            curr_max = prefix-m            
            if curr_max > answer:
                answer = curr_max
            if curr_max < 0:
                m = prefix
        return answer