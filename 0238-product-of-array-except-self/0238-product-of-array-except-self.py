class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]
        prod = 1
        for i in range(n-1):
            prod *= nums[i]
            answer.append(prod)
        prod = 1
        for i in range(n-1):
            prod *= nums.pop()
            answer[n-2-i] *= prod
        return answer