class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(len(matrix[0]))]
        
        for row in matrix:
            for j, val in enumerate(row):
                res[j].append(val)
        
        return res