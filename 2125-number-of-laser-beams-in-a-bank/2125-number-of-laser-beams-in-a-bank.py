class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            c = row.count("1")
            if c:
                ans += prev * c
                prev = c
        return ans