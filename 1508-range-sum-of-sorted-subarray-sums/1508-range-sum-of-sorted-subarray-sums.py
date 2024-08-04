class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        
        arr = []
        for i in range(n):
            for j in range(i+1, n+1):
                arr.append(pre[j]-pre[i])
        arr.sort()
        
        return sum(arr[left-1:right]) % (10 ** 9 + 7)