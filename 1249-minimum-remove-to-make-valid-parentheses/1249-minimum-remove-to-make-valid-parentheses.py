class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        curr = 0
        idxs = []
        
        for i, ch in enumerate(s):
            if ch == "(":
                curr += 1
                idxs.append(len(ans))
                ans.append(ch)
            elif ch == ")":
                if curr == 0:
                    continue
                else:
                    curr -= 1
                    ans.append(ch)
            else:
                ans.append(ch)
        
        
        to_del = idxs[len(idxs)-curr:]
        to_del.reverse()
                
        ans1 = []
        for j in range(len(ans)):
            if to_del and j == to_del[-1]:
                to_del.pop()
            else:
                ans1.append(ans[j])
        return "".join(ans1)
        