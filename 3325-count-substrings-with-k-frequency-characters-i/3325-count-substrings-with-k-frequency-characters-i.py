class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        idxs = [[] for _ in range(26)]
        M = -1
        ans = 0
        ok = False
        for i in range(len(s)):
            idx = ord(s[i])-ord('a') 
            idxs[idx].append(i)
            if len(idxs[idx]) >= k:
                M = max(M, idxs[idx][-k])
            ans += M + 1
        return ans