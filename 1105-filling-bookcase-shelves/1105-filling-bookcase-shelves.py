class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            maxWidth = shelfWidth
            maxHeight = 0
            j = i - 1
            while j >= 0 and maxWidth - books[j][0] >= 0:
                maxWidth -= books[j][0]
                maxHeight = max(maxHeight, books[j][1])
                dp[i] = min(dp[i], dp[j] + maxHeight)
                j -= 1
        return dp[n]