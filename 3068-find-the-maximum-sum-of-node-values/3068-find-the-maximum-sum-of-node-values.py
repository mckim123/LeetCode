class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        INF = -10 ** 9 - 1

        def dfs(node, parent):
            max1 = nums[node]
            max2 = nums[node] ^ k

            child_sums = 0
            child_diffs = []

            for child in graph[node]:
                if child != parent:
                    child_sum1, child_sum2 = dfs(child, node)
                    child_sums += child_sum1
                    heapq.heappush(child_diffs, child_sum1 - child_sum2)

            max1 += child_sums
            max2 += child_sums
            max11 = max21 = INF

            if child_diffs:
                child_diffs1 = child_diffs[:]
                curr = heapq.heappop(child_diffs1)
                max11 = (nums[node] ^ k) + child_sums - curr
                max21 = nums[node] + child_sums - curr

                while len(child_diffs1) >= 2:
                    curr = heapq.heappop(child_diffs1) + heapq.heappop(child_diffs1)
                    if curr < 0:
                        max11 -= curr
                        max21 -= curr
                    else:
                        break

            while len(child_diffs) >= 2:
                curr = heapq.heappop(child_diffs) + heapq.heappop(child_diffs)
                if curr < 0:
                    max1 -= curr
                    max2 -= curr
                else:
                    break

            return max(max1, max11), max(max2, max21)

        return dfs(0, -1)[0]
