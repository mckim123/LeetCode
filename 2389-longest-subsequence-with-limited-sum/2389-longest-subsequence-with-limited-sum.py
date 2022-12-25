from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return [bisect_right(nums, x) for x in queries]
