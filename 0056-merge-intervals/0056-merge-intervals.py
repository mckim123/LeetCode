class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        curr = None
        
        for x, y in intervals:
            if curr != None:
                if curr[1] >= x:
                    curr[1] = max(curr[1], y)
                    continue
                else:
                    answer.append(curr)
            curr = [x,y]
        answer.append(curr)
        
        return answer