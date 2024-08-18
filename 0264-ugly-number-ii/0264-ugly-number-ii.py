class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set()
        s.add(1)
        h = [1]
        for _ in range(n-1):
            cur = heappop(h)
            cur1 = cur * 2
            if cur1 not in s:
                heappush(h, cur1)
                s.add(cur1)
            cur2 = cur * 3
            if cur2 not in s:
                heappush(h, cur2)
                s.add(cur2)
            cur3 = cur * 5
            if cur3 not in s:
                heappush(h, cur3)
                s.add(cur3)
            s.remove(cur)
        return heappop(h)