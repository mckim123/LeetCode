class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()         # (sum, start_index)의 형태로 저장
        res = -int(1e4)
        
        for i, num in enumerate(nums):
            if num >= 0:
                while queue and queue[0][1] + k < i:
                    queue.popleft()
                last = 0
                if queue:
                    last = queue[0][0]
                res = max(res, num + last)
                queue.clear()
                queue.append((num + last, i))

            else:
                res = max(res, num)
            
                while queue and queue[0][1] + k < i:
                    queue.popleft()
                        
                if not queue:
                    continue
    
                if queue[0][0] + num <= 0:
                    continue
                
                else:
                    curr_val = queue[0][0] + num
                    while queue and queue[-1][0] <= curr_val:
                        queue.pop()
                    queue.append((curr_val, i))
                
        return res
