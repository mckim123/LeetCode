class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        a = [(v, -k) for k, v in c.items()]
        a.sort()
        ans = []
        for v, k in a:
            ans.extend([-k]*v)
        return ans
        