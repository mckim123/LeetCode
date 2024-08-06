class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        values = sorted(c.values(), reverse= True)
        ans = 0
        for i, v in enumerate(values):
            ans += v * (i// 8 + 1)
        return ans