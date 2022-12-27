import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        heapq.heapify(capacity)
        answer = 0
        while(capacity):
            additionalRocks -= heapq.heappop(capacity)
            if additionalRocks < 0:
                return answer
            answer += 1
        return answer