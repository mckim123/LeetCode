class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counter = [0] * n
        for row in grid:
            k = row[0]
            for i, num in enumerate(row):
                if k == num:
                    counter[i] += 1
        ans = 0
        for i in range(n):
            c = counter[i]
            ans += (1 << (n-1-i)) * max(c, m-c)
        
        return ans