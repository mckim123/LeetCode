class Solution:
    def minimizeStringValue(self, s: str) -> str:
        c = Counter(s)
        h = []
        for ch in "abcdefghijklmnopqrstuvwxyz":
            h.append((c[ch], ch))
        left = c["?"]
        to_add = dict()

        heapq.heapify(h)
        while left:
            val, ch = heapq.heappop(h)
            left -= 1
            if ch not in to_add:
                to_add[ch] = 0
            to_add[ch] += 1
            heapq.heappush(h, (val+1, ch))
        
        k = sorted(to_add.keys(), reverse=True)

        ans = []
        for ch in s:
            if ch != "?":
                ans.append(ch)
            else:
                ans.append(k[-1])
                to_add[k[-1]] -= 1
                if to_add[k[-1]] == 0:
                    del to_add[k[-1]]
                    k.pop()
        return "".join(ans)