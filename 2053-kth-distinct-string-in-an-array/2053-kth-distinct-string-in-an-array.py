class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        left = k
        for s in arr:
            if c[s] == 1:
                left -= 1
                if not left:
                    return s
        return ""