# This segment tree has 4 values for each node
# min, max, len, d
# d is the least common divisor of all differences in the range
# merge could be calculated by:
#   min = min(min(left), min(right))
#   max = max(max(left), max(right))
#   len = len(left) + len(right)
#   d = gcd(d(left), d(right), min(right) - min(left))
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [[None, None, 0, 0] for _ in range(self.n * 4)]
        self.build(nums, 1, 0, self.n-1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = [nums[start], nums[start], 1, 0]
        else:
            mid = (start + end) // 2
            self.build(nums, node * 2, start, mid)
            self.build(nums, node * 2 + 1, mid + 1, end)

            left = self.tree[node * 2]
            right = self.tree[node * 2 + 1]
            self.tree[node] = [min(left[0], right[0]), max(left[1], right[1]), left[2] + right[2],
                               self.gcd(left[3], right[3], right[0] - left[1])]

    def gcd(self, a, b, c):
        return math.gcd(math.gcd(a, b), c)

    # query determines if there is an arithmetic subarray within the range and returns a boolean value
    # it is guaranteed that the range do not have duplicates
    # it splits the range up to 2 * log(n) nodes (which fully covers the range and do not intersect)
    # then it calculates the global min, max, len
    # we can get the expected d by (max - min) // (len - 1)
    # and just need to check whether the d is a divisor of all d_i, a_i - global_min
    def query(self, left, right):
        total_nodes = self._query(1, 0, self.n-1, left, right)
        total_min = min(self.tree[node][0] for node in total_nodes)
        total_max = max(self.tree[node][1] for node in total_nodes)
        total_len = sum(self.tree[node][2] for node in total_nodes)

        expected_d = (total_max - total_min) // (total_len - 1)
        if expected_d * (total_len - 1) != total_max - total_min:
            return False

        for node in total_nodes:
            if self.tree[node][3] % expected_d != 0:
                return False
            if (self.tree[node][1] - total_min) % expected_d != 0:
                return False

        return True

    def _query(self, node, start, end, left, right):
        # If the current segment is completely outside the query range
        if right < start or left > end:
            return []

        # If the current segment is completely inside the query range
        if left <= start and end <= right:
            return [node]

        # Handles partial overlap of the current segment with the query range
        mid = (start + end) // 2
        left_nodes = self._query(node*2, start, mid, left, right)
        right_nodes = self._query(node*2+1, mid+1, end, left, right)

        return left_nodes + right_nodes


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n, m = len(nums), len(l)

        indices = defaultdict(list)     # {num: reversed([indices])}
        conn_indices = []               # [start, end] which are identical

        curr = nums[0]
        count = 0
        for i in range(n):
            indices[nums[i]].append(i)
            if curr != nums[i]:
                if count > 1:
                    conn_indices.append([i-count, i-1]) # [start, end] which are identical
                count = 1
                curr = nums[i]
            else:
                count += 1
        if count > 1:
            conn_indices.append([n-count, n-1])

        for val in indices.values():
            val.reverse()

        segTree = SegmentTree(nums)

        max_rs_without_duplicate = self.getMaxRsWithoutDuplicate(n, nums, indices)
        ans = []
        for i in range(m):
            left, right = l[i], r[i]
            if right <= left + 1:
                ans.append(True)
                continue

            # If there are duplicates, then it returns True if and only if all values are the same
            if max_rs_without_duplicate[left] < right:
                if not conn_indices:
                    ans.append(False)
                    continue
                i1 = bisect.bisect_right(conn_indices, [left, n])
                if not i1:
                    ans.append(False)
                    continue
                l1, r1 = conn_indices[i1-1]
                ans.append(r1 >= right)
                continue

            else:
                ans.append(segTree.query(left, right))

        return ans

    # This method calculates the maximum right index that can be reached without encountering duplicates
    def getMaxRsWithoutDuplicate(self, n, nums, indices):
        res = [n-1] * n
        cursor = 0
        curr_limit_queue = deque()

        for i in range(n):
            if curr_limit_queue and curr_limit_queue[0][1] == i:
                end, _ = curr_limit_queue.popleft()
                for j in range(cursor, end+1):
                    res[j] = i-1
                    cursor += 1
            num = nums[i]
            indices[num].pop()
            if indices[num]:
                next_idx = indices[num][-1]
                while curr_limit_queue and curr_limit_queue[-1][1] > next_idx:
                    curr_limit_queue.pop()
                curr_limit_queue.append([i, next_idx])
        return res
        