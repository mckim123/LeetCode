class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set()
        s.add(1)
        h = [1]
        j = n-1
        while j:
            cur = heappop(h)
            if cur * 2 not in s:
                heappush(h, cur * 2)
                s.add(cur * 2)
            if cur * 3 not in s:
                heappush(h, cur * 3)
                s.add(cur * 3)
            if cur * 5 not in s:
                heappush(h, cur * 5)
                s.add(cur * 5)
            j -= 1
        return heappop(h)