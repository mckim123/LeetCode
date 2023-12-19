class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        counts = [[1] * n for _ in range(m)]
        sums = [img[i][:] for i in range(m)]
        
        dx = [0, 0, 1, 1, 1,-1,-1,-1]
        dy = [1, -1,1,-1, 0, 1,-1, 0]
        
        for i in range(m):
            for j in range(n):
                val = img[i][j]
                for k in range(8):
                    i1 = i + dx[k]
                    j1 = j + dy[k]
                    if i1 < 0 or j1 < 0 or i1 == m or j1 == n:
                        continue
                    sums[i1][j1] += val
                    counts[i1][j1] += 1

        for i in range(m):
            for j in range(n):
                sums[i][j] //= counts[i][j]
        
        return sums