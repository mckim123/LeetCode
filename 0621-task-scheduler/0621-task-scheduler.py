class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        c = Counter(tasks)
        h = [(-v, i) for i, v in c.items()]
        heapq.heapify(h)
        keep = []
        
        while h or keep:
            t += 1
            if keep and keep[0][0] == t:
                _, v, i = heapq.heappop(keep)
                heapq.heappush(h, (v, i))
            if h:
                v, i = heapq.heappop(h)
                if v == -1:
                    continue
                heapq.heappush(keep, (n+t+1, v+1, i))
        return t