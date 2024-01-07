class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        one_nums = defaultdict(int)
        cands = dict()
        
        for num in nums:
            one_nums[num] += 1
            for num1, v in one_nums.items():
                if num1 == num:
                    continue
                k1 = 2 * num - num1
                if k1 not in cands:
                    cands[k1] = defaultdict(int)
                cands[k1][num - num1] += v
                ans += v
            
            if num not in cands:
                continue
            for d, v in cands[num].items():
                k1 = num + d
                if k1 not in cands:
                    cands[k1] = defaultdict(int)
                cands[k1][d] += v
                ans += v

        for i, v in one_nums.items():
            if v == 1:
                continue
            ans += 2 ** v - 1 - v
        
        ans -= (n * (n-1)) // 2

        return ans