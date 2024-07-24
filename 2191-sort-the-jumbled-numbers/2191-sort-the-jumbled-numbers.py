class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        rev = [-1] * 10
        for i in range(10):
            rev[mapping[i]] = i
        
        a = [(int("".join(map(lambda x:str(mapping[int(x)]), list(str(num))))), i, len(str(num))) for i, num in enumerate(nums)]
        a.sort()
        ans = []
        for num, _, l in a:
            l1 = list(map(lambda x:str(rev[int(x)]), list(str(num))))
            ans.append(int("".join([str(rev[0])] * (l - len(l1)) + l1)))
        return ans