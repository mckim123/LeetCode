class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {v:i for i, v in enumerate(nums)}
        ans = 0
        reps = 0
        idx = 0
        
        for num in sorted(nums):
            if pos[num] < idx:
                idx = pos[num]
                reps += 1
                ans += reps
            else:
                idx = pos[num]
                ans += reps    
        
        return ans + n
    