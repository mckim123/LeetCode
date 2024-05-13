class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(n):
            grid[0][n-1-i] = int(grid[0][n-1-i] == grid[0][0])
        
        for i in range(1, m):
            row = grid[i]
            k = row[0]
            for i, num in enumerate(row):
                if k == num:
                    grid[0][i] += 1
        ans = 0
        for i, c in enumerate(grid[0]):
            ans += max(c, m-c) << (n-1-i)
        
        return ans