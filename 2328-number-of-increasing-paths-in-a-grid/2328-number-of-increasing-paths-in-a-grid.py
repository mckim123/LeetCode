class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        INF = 10 ** 9 + 7
        
        # 각 칸별로 각 칸에서 종료되는 개수를 a[m][n]이라고 하고, DP를 사용
        m = len(grid)
        n = len(grid[0])
        a = [[-1] * n for _ in range(m)]

        
        def dp(i, j):
            if a[i][j] != -1:
                return a[i][j]
            
            curr_value = grid[i][j]
            curr_count = 1
            
            for k in range(4):
                i1 = i + dr[k]
                j1 = j + dc[k]
                if 0 <= i1 < m and 0 <= j1 < n and grid[i1][j1] < curr_value:
                    curr_count += dp(i1, j1)
                    curr_count %= INF
            
            a[i][j] = curr_count
            return curr_count

                
        for i in range(m):
            for j in range(n):
                if a[i][j] == -1:
                    dp(i, j)
        
        return sum([sum(b)% INF for b in a]) % INF