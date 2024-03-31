class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i, num in enumerate(nums):
            if num in s:
                return [s[num], i]
            else:
                s[target-num] = i