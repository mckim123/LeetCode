class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = [[10 ** 5 + 1] * len(matrix), [-1] * len(matrix[0])]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lucky[0][i] = min(lucky[0][i], matrix[i][j])
                lucky[1][j] = max(lucky[1][j], matrix[i][j])
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if lucky[0][i] == matrix[i][j] == lucky[1][j]:
                    ans.append(matrix[i][j])
        return ans