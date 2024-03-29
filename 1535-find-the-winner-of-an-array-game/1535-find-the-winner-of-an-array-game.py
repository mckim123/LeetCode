class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        prev_winner = arr[0]
        streak = -1
        for curr in arr:
            if prev_winner >= curr:
                streak += 1
            else:
                prev_winner = curr
                streak = 1
            if streak == k:
                break
        return prev_winner