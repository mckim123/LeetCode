class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 0 if 0 in nums else -10
        while(0 in nums):
            answer = max(answer, self.findMaxWithoutZero(nums[:nums.index(0)]))
            nums = nums[nums.index(0)+1:]
        answer = max(answer, self.findMaxWithoutZero(nums))
        return answer
    
    def findMaxWithoutZero(self, nums):
        n = len(nums)
        if n == 0:
            return -10
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1], nums[0]*nums[1])
        else:
            max_prod = 1
            prod = 1
            for num in nums:
                prod *= num
                if prod > max_prod:
                    max_prod = prod
            prod = 1
            for _ in range(n):
                prod *= nums.pop()
                if prod > max_prod:
                    max_prod = prod
            return max_prod