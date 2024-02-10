class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                curr = True
                for k in range((j-i)//2 + 1):
                    if s[i+k] != s[j-k]:
                        curr = False
                        break
                if curr:
                    ans += 1
        return ans