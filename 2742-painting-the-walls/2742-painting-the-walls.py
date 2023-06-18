class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        point = [t+1 for t in time]
        n = len(cost)
        max_point = min(sum(point), n+max(point))
        dp = [10**6 * n] * (max_point + 1)
        dp[0] = 0
        for i, curr_cost in enumerate(cost):
            for j in range(max_point, point[i] - 1, -1):
                dp[j] = min(dp[j], dp[j - point[i]] + curr_cost)
        return min(dp[n:])