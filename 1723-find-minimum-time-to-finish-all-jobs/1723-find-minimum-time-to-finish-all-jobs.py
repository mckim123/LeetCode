class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 주요 아이디어 : 평균을 넘겼다면 더이상 추가하지 않는 것이 반드시 더 최적인 케이스
        n = len(jobs)
        curr_max = 0
        jobs.sort()
        
        if n == k:
            return max(jobs)
        
        # n이 2k보다 작은 경우 상위 2k-n개의 job은 단독으로 선택하는 것이 최적임을 증명 가능(다른 것을 단독으로 사용하는 것보다 효율적)
        # -> 이 과정을 통해 k를 반드시 6 이하로 줄일 수 있음
        elif n < 2 * k:
            curr_max = jobs[-1]
            jobs = jobs[:2*(n-k)]
            k = n-k
        
        sum_jobs = sum(jobs)
        
        # 단독으로 사용하는 것이 이미 평균을 넘긴다면 단독으로 사용하도록 처리
        while jobs and k * jobs[-1] >= sum_jobs:
            sum_jobs -= jobs[-1]
            curr_max = max(curr_max, jobs.pop())
            k -= 1
        
        if not jobs:
            return curr_max
        
        presums = [sum(jobs[:i+1]) for i in range(len(jobs))] 
        # 부동소수점 오차 조정용
        ep = 1e-3
        
        def backtrack(nums, i, valid_count):  # nums : jobs 누적 합 sorted(rev) 버전 / 현재 남은 job들이 추가될 수 있는 후보들의 job 합, i : 현재 추가할 job index(뒤부터), valid_count : 0이 아닌 nums 개수 보관용
            # 한명 남은 경우
            if len(nums) == 1:
                return nums[0] + presums[i]
            
            # 마지막 job인 경우
            if i == 0:
                return max(nums[0], nums[-1] + jobs[0])
            
            # 모두 0인 경우 -> 아무나 넣으면 됨
            if not valid_count:
                nums[0] += jobs[i]
                return backtrack(nums, i-1, 1)
            
            res = presums[-1]
            # bound 이상인 경우 더이상 추가할 일 없음
            bound = (sum(nums) + presums[i]) / len(nums) - ep
            
            # 
            for j in range(valid_count):
                # 이 job을 받으면 졸업인 경우
                if nums[j] + jobs[i] >= bound:
                    # 더 작은 것에 넣어도 넘친다면 스킵
                    if j+1 < valid_count and nums[j+1] + jobs[i] >= bound:
                        continue
                    else:
                        res = max(nums[j] + jobs[i], backtrack(nums[:j] + nums[j+1:], i-1, valid_count - 1))
                
                else:
                    nums1 = nums.copy()
                    nums1[j] += jobs[i]
                    res = min(res, backtrack(sorted(nums1, reverse = True), i-1, valid_count))
            
            # 남아있는 0이 존재하는 경우
            if valid_count < len(nums):
                nums1 = nums.copy()
                nums1[valid_count] = jobs[i]
                res = min(res, backtrack(sorted(nums1, reverse = True), i-1, valid_count + 1))
            
            return res
        
        return max(curr_max, backtrack([0] * k, len(jobs)-1, 0))