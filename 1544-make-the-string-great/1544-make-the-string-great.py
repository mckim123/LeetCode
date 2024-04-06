class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for ch in s:
            if ans and ord(ans[-1]) ^ ord(ch) == 32:
                ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)