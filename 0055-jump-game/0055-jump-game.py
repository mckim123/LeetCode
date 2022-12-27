class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        reachableIndex = 0
        n = len(nums)
        while pos <= reachableIndex:
            temp = nums[pos] + pos
            if temp > reachableIndex:
                reachableIndex = temp
                if temp >= n:
                    return True
            pos += 1
        return reachableIndex+1 >= n