import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        requires = [x-y for x,y in zip(capacity, rocks)]
        heapq.heapify(requires)
        answer = 0
        while(requires):
            additionalRocks -= heapq.heappop(requires)
            if additionalRocks < 0:
                return answer
            answer += 1
        return answer