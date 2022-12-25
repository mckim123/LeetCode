class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            a = nums.pop()
            if a in s:
                return True
            s.add(a)
        return False
        # return len(set(nums)) < len(nums)