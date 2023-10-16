class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {v:i for i, v in enumerate(nums)}
        ans = 0
        reps, idx = 0, 0
        nums.sort()
        
        for num in nums:
            if pos[num] < idx:
                reps += 1
            idx = pos[num]
            ans += reps    
        
        return ans + len(nums)
    