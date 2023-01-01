class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        answer = ""
        if x < 0:
            answer += "-"
            x *= -1
        ans = int(answer + str(x).rstrip("0")[::-1])
        if -2**31 <= ans < 2**31:
            return ans
        return 0