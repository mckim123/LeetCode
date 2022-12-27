import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort(reverse = True)
        answer = 0
        while(capacity):
            additionalRocks -= capacity.pop()
            if 0 > additionalRocks:
                return answer
            answer += 1
        return answer