class LazySegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _update_range(self, node, start, end, l, r, value):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[node * 2] += value
                self.lazy[node * 2 + 1] += value
            return

        mid = (start + end) // 2
        self._update_range(node * 2, start, mid, l, r, value)
        self._update_range(node * 2 + 1, mid + 1, end, l, r, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update_range(self, l, r, value):
        self._update_range(1, 0, self.size - 1, l, r, value)

    def _query_range(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return 0

        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self._query_range(node * 2, start, mid, l, r)
        right_sum = self._query_range(node * 2 + 1, mid + 1, end, l, r)
        return left_sum + right_sum

    def query_range(self, l, r):
        return self._query_range(1, 0, self.size - 1, l, r)

    
class Solution:
    def sumCounts(self, nums):
        MOD = 1_000_000_007
        segment_tree = LazySegmentTree(len(nums))
        last_seens = defaultdict(int)                           # last_seens[num] : last seen index + 1
        curr_sq, ans = 0, 0                                     # curr_sq : sum of squares of distinct counts of all subarrays ending with curr_index

        for i, num in enumerate(nums):
            last_seen = last_seens[num]
            
            # update curr_sq
            # all counts in index from last_seen to i is increased by 1, so their sum of squares are increased by (2 * value + 1) for each
            curr_sq = (curr_sq + 2 * segment_tree.query_range(last_seen, i) + i - last_seen + 1) % MOD
            ans = (ans + curr_sq) % MOD
            
            # update values
            segment_tree.update_range(last_seen, i, 1)
            last_seens[num] = i + 1

        return ans