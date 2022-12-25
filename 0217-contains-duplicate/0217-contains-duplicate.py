class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
        # return len(set(nums)) < len(nums)