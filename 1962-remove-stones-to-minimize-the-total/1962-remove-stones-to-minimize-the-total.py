import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapq.heapify(piles)
        for _ in range(k):
            temp = heapq.heappop(piles)
            heapq.heappush(piles, temp + (-temp) // 2)
        return -sum(piles) 