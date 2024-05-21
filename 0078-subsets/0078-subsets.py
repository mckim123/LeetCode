class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [set()]
        for num in nums:
            ans1 = []
            for s in ans:
                s1 = s.copy()
                s1.add(num)
                ans1.append(s1)
            ans += ans1
        return ans