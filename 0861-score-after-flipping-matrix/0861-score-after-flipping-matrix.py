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
        curr = 1
        for c in reversed(counter):
            ans += max(c, m-c) * curr
            curr <<= 1
        
        return ans