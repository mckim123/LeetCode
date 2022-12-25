class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 0 if 0 in nums else -10
        while(0 in nums):
            answer = max(answer, findMaxWithoutZero(nums[:nums.index(0)]))
            nums = nums[nums.index(0)+1:]
        answer = max(answer, findMaxWithoutZero(nums))
        return answer
    
def findMaxWithoutZero(nums):
    if len(nums) == 0:
        return -10
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1], nums[0]*nums[1])
    else:
        max_prod = 1
        prod = 1
        for num in nums:
            prod *= num
            if prod > max_prod:
                max_prod = prod
        prod = 1
        while(nums):
            prod *= nums.pop()
            if prod > max_prod:
                max_prod = prod
        return max_prod