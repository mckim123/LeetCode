class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        prev_winner = arr[0]
        streak = 0
        for i in range(1, len(arr)):
            curr = arr[i]
            if prev_winner > curr:
                streak += 1
            else:
                prev_winner = curr
                streak = 1
            if streak == k:
                return prev_winner
        return prev_winner