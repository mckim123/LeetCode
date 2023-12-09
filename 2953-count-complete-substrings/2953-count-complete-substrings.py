class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(word):
            indices[c].append(i)

        ends = {i:[-1, -1] for i in range(len(word))}

        for c in indices:
            indices[c].append(-1)
            for i in range(len(indices[c])-k):
                ends[indices[c][i]][1] = indices[c][i+k]
                ends[indices[c][i]][0] = indices[c][i+k-1]

        def find(l, r):
            return sum(findstart(i, r) for i in range(l, r))

        @lru_cache(None)
        def findstart(i, r):
            if i >= r:
                return 0
            last = ends[i][0]
            if last == -1:
                return 0
            if last >= r:
                return 0
            if ends[i][1] != -1:
                r = min(r, ends[i][1])

            curr_count = 1
            visited = {word[i]}

            res = 0

            if last - i + 1 == k * curr_count:
                return 1 + findstart(last + 1, r)

            for j in range(i+1, r):
                if word[j] in visited:
                    continue
                visited.add(word[j])
                curr_count += 1
                if ends[j][0] == -1 or ends[j][0] >= r:
                    return 0
                last = max(last, ends[j][0])
                if ends[j][1] != -1:
                    r = min(r, ends[j][1])
                if last - i + 1 == k * curr_count:
                    return 1 + findstart(last+1, r)
            return 0

        prev = ord(word[0])
        cut = [0]
        for i, ch in enumerate(word):
            if abs(ord(ch) - prev) > 2:
                cut.append(i)
            prev = ord(ch)

        cut.append(len(word))

        ans = 0
        for i in range(len(cut)-1):
            if cut[i+1] - cut[i] < k:
                continue
            ans += find(cut[i], cut[i+1])
        return ans
