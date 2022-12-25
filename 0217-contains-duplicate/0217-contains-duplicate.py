class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set()
        for _ in range(n):
            a = nums.pop()
            if a in s:
                return True
            s.add(a)
        return False
        # return len(set(nums)) < len(nums)