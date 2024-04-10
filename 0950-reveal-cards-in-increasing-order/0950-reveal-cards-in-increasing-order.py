class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque(range(len(deck)))
        idx = []
        i = 0
        
        ans = [0] * len(deck)
        
        while q:
            ans[q.popleft()] = deck[i]
            i += 1
            if q:
                q.append(q.popleft())
        
        return ans
