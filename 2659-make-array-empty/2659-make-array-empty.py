class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {v:i for i, v in enumerate(nums)}
        ans = 0
        reps, idx = 0, 0
        
        for num in sorted(nums):
            if pos[num] < idx:
                reps += 1
            idx = pos[num]
            ans += reps    
        
        return ans + len(nums)
    