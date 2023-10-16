class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = sorted(nums)
        index = dict()
        pos = [-1] * len(nums)
        ans = 0
        
        for i, num in enumerate(nums1):
            index[num] = i
        
        for i in range(n):
            nums[i] = index[nums[i]]
            pos[nums[i]] = i
        
        reps = 0
        idx = 0
        
        for i in range(n):
            if pos[i] < idx:
                idx = pos[i]
                reps += 1
                ans += reps
            else:
                idx = pos[i]
                ans += reps
        
        return ans + n