class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        bit = 0
        keep = []
        for num in nums:
            m, M = num, num ^ k
            if m > M:
                m, M = M, m
            else:
                bit ^= 1
            ans += m
            keep.append(M-m)
            keep.sort()
            if len(keep) >= 3:
                ans += keep.pop()
                ans += keep.pop()
        if bit:
            keep.pop(0)
        return ans + sum(keep)