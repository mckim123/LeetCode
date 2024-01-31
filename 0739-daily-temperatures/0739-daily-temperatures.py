class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while h and h[0][0] < t:
                _, i1 = heapq.heappop(h)
                ans[i1] = i-i1
            heapq.heappush(h, (t, i))
        return ans