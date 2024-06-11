class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        c = [0] * len(arr2)
        idxs = {}
        for i, num in enumerate(arr2):
            idxs[num] = i
        
        for num in arr1:
            if num in idxs:
                c[idxs[num]] += 1
            else:
                res.append(num)
        
        res.sort()
        ans = []
        
        for i, v in enumerate(c):
            if not v:
                continue
            else:
                ans.extend([arr2[i]] * v)
        
        return ans + res