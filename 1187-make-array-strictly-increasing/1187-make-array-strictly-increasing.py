import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        INF = 10**9+1
        arr2 = list(set(arr2))
        arr2.sort()
        
        prev = [-1]  # prev[i] means the minimum value of prev index value with i exchanges
        count = 0
        
        for i in range(len(arr1)):
            curr = [INF] * (len(prev)+1)
            curr_value = arr1[i]
            for j, prev_value in enumerate(prev):
                if curr_value > prev_value:
                    curr[j] = min(curr[j], curr_value)
                    curr[j+1] = min(curr[j+1], curr_value)
                min_greater_value = self.find_gt(arr2, prev_value)
                if min_greater_value > prev_value:
                    curr[j+1] = min(curr[j+1], min_greater_value)
            
            curr_count = 0

            while curr_count < len(curr) and curr[curr_count] == INF:
                curr_count += 1
            
            if curr_count == len(curr):
                return -1
            count += curr_count
            prev = curr[curr_count:]
            
            
        return count
                
    def find_gt(self, a, x):
        i = bisect_right(a, x)
        if i != len(a):
            return a[i]
        return -1
    
    
    
    '''
    1, 5, 3, 6, 7   /    1, 2, 3, 4
    이전 [-1]
    다음 [1, 1]
    다음 [5, 2, 2]
    다음 [3, 3, 3]  count = 1
    다음 [6, 6, 6, 6] count = 1
    다음 [7, 7, 7, 7, 7] count = 1
    
    
    1, 5, 3, 6, 7   /    1, 3, 4
    이전 [-1]
    다음 [1, 1]
    다음 [5, 3, 3]
    다음 [(x, x,) 4, 4, 4]  count = 2
    다음 [6, 6, 6, 6] count = 2
    다음 [7, 7, 7, 7, 7] count = 2
    
    1, 5, 3, 6, 7   /    1, 3, 6
    이전 [-1]
    다음 [1, 1]
    다음 [5, 3, 3]
    다음 [x, 6, 6, 6]  count = 1
    다음 [x, x, x, x, x] count = 1
    다음 [7, 7, 7, 7, 7] count = 1
    
    
    '''