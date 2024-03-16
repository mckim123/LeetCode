class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        h = []
        for i, num in enumerate(nums):
            heapq.heappush(h, (num, i))
        marked = set()
        s = sum(nums)
        ans = []
        
        for i, k in queries:
            if i not in marked:
                s -= nums[i]
                marked.add(i)
            curr = k
            while curr and h:
                val, idx = heapq.heappop(h)
                if idx in marked:
                    continue
                marked.add(idx)
                s -= val
                curr -= 1
            ans.append(s)
        return ans