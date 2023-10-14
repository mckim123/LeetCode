class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        curr_max = 0
        jobs.sort()
        
        if n == k:
            return max(jobs)
        
        elif n < 2 * k:
            curr_max = jobs[-1]
            jobs = jobs[:2*(n-k)]
            k = n-k
        
        sum_jobs = sum(jobs)
        
        while jobs and k * jobs[-1] >= sum_jobs:
            sum_jobs -= jobs[-1]
            curr_max = max(curr_max, jobs.pop())
            k -= 1
        
        if not jobs:
            return curr_max
        
        presums = [sum(jobs[:i+1]) for i in range(len(jobs))] 
        ep = 1e-3
        
        def backtrack(nums, i, valid_count):  # nums : jobs 누적 합 sorted 버전, i : 현재 추가할 job index(뒤부터), valid_count
            if len(nums) == 1:
                return nums[0] + presums[i]
            
            if i == 0:
                return max(nums[0], nums[-1] + jobs[0])
            
            if not valid_count:
                nums[0] += jobs[i]
                return backtrack(nums, i-1, 1)
            
            res = presums[-1]
            bound = (sum(nums) + presums[i]) / len(nums) - ep
            
            for j in range(valid_count):
                if nums[j] + jobs[i] >= bound:
                    if j+1 < valid_count and nums[j+1] + jobs[i] >= bound:
                        continue
                    else:
                        res = max(nums[j] + jobs[i], backtrack(nums[:j] + nums[j+1:], i-1, valid_count - 1))
                
                else:
                    nums1 = nums.copy()
                    nums1[j] += jobs[i]
                    res = min(res, backtrack(sorted(nums1, reverse = True), i-1, valid_count))
            
            if valid_count < len(nums):
                nums1 = nums.copy()
                nums1[valid_count] = jobs[i]
                res = min(res, backtrack(sorted(nums1, reverse = True), i-1, valid_count + 1))
            
            return res
        
        return max(curr_max, backtrack([0] * k, len(jobs)-1, 0))