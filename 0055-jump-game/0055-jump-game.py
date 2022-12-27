class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        reachableIndex = 0
        while pos <= reachableIndex:
            temp = nums[pos] + pos
            if temp > reachableIndex:
                reachableIndex = temp
                if temp >= len(nums):
                    return True
            pos += 1
        return reachableIndex+1 >= len(nums)