class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        k -= 1
        while k:
            res ^= k & 1
            k >>= 1
        return res