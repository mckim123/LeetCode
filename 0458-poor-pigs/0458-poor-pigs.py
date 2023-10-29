class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie
        ans = 0
        while buckets > 1:
            buckets /= (T+1)
            ans += 1
        return ans