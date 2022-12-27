import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        for i in range(n):
            capacity[i] -= rocks[i]
        capacity.sort(reverse = True)
        answer = 0
        for _ in range(n):
            additionalRocks -= capacity.pop()
            if 0 > additionalRocks:
                return answer
            answer += 1
        return answer