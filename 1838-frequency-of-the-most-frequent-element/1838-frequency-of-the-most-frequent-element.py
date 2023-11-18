class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        queue = deque()
        curr = 0
        curr_count = 0
        ans = 0
    
        for key in sorted(c.keys()):
            k -= curr_count * (key - curr)
            while k < 0:
                val, count = queue[0]
                needs = -(k // (key - val))
                if count > needs:
                    queue[0][1] -= needs
                    k += needs * (key - val)
                    curr_count -= needs
                else:
                    queue.popleft()
                    k += count * (key - val)
                    curr_count -= count
            
            curr_count += c[key]
            queue.append([key,c[key]])
            curr = key
            ans = max(ans, curr_count)
        
        return ans