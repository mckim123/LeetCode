class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_occ = max(c.values())
        ans = 0
        for v in c.values():
            if v == max_occ:
                ans += v
        return ans