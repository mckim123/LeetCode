class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzags = [""]*numRows
        n = 2 * (numRows - 1)
        indices = list(range(numRows)) + list(range(numRows-2,0,-1))
        for i, letter in enumerate(list(s)):
            zigzags[indices[i%n]] += letter
        return "".join(zigzags)