class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        ans = 0
        
        for i, num in enumerate(sorted(c.keys())):
            val = c[num]
            ans += val * i
        
        return ans