class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1]
        suffixes = [1]
        answer = []
        prefix = 1
        suffix = 1
        for i in range(n-1):
            prefix *= nums[i]
            prefixes.append(prefix)
            suffix *= nums[n-1-i]
            suffixes.append(suffix)
        for i in range(n):
            answer.append(prefixes[i]*suffixes[n-1-i])
        return answer