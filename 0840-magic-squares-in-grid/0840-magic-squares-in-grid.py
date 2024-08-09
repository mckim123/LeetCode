class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                a = set()
                for i1 in range(3):
                    s = 0
                    for j1 in range(3):
                        val = grid[i+i1][j+j1]
                        if val in a or val > 9:
                            break
                        a.add(val)
                        s += val
                    if s != 15:
                        break
                if len(a) == 9:
                    if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 and grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] == 15 and  grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 and  grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15:
                        ans += 1
        return ans