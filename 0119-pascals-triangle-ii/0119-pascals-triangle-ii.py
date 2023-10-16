class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            next_ans = ans.copy()
            next_ans.append(0)
            
            for j in range(i+1):
                next_ans[i+1-j] += ans[j]
            ans = next_ans
        
        return ans