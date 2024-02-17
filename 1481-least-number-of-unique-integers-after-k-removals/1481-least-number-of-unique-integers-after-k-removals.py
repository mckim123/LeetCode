class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        v = sorted(c.values(), reverse = True)
        
        ans = len(c)
        while k > 0 and v:
            curr = v.pop()
            if k >= curr:
                k -= curr
                ans -= 1
            else:
                break
        return ans