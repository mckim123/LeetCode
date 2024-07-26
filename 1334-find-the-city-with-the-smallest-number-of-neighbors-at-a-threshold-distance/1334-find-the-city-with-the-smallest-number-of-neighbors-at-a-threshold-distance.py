class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        dists = [[dt+1] * n for _ in range(n)]
        
        for s, e, w in edges:
            dists[s][e] = w
            dists[e][s] = w
        
        for i in range(n):
            dists[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
                
        mn = n
        ans = -1
        for i in range(n):
            row = dists[i]
            neis = sum(int(v <= dt) for v in row) - 1
            if neis <= mn:
                mn = neis
                ans = i
        return ans            
            