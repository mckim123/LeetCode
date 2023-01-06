import heapq

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        count = 0
        while(costs):
            temp = heapq.heappop(costs)
            if temp <= coins:
                count += 1
                coins -= temp
        return count