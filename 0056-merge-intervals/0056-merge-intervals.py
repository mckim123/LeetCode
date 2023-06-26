class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        curr = None
        
        for x, y in intervals:
            if curr == None:
                curr = [x,y]
            else:
                if curr[1] >= x:
                    curr[1] = max(curr[1], y)
                else:
                    answer.append(curr)
                    curr = [x,y]
        
        if curr != None:
            answer.append(curr)
        
        return answer