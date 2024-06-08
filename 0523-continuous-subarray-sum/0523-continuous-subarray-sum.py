class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = {0}
        c = 0
        pc = 0
        for num in nums:
            c = (c + num) % k
            if c in s:
                if pc == c:
                    pc = -1
                    continue
                return True
            s.add(c)
            pc = c
        return False