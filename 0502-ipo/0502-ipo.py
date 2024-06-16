class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        h1 = [(capital[i], profits[i]) for i in range(n)]
        heapify(h1)
        h2 = []
        
        while k > 0:
            while h1 and h1[0][0] <= w:
                heappush(h2, -heappop(h1)[1])
            if not h2:
                break
            else:
                k -= 1
                w -= heappop(h2)
        
        return w