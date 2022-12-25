class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        n = len(nums)
        small, large = 0, n-1
        sum = sorted_nums[small] + sorted_nums[large]
        while sum != target:
            if sum > target:
                large -= 1
            else:
                small += 1
            sum = sorted_nums[small] + sorted_nums[large]
        small_index = nums.index(sorted_nums[small])
        large_index = nums.index(sorted_nums[large])
        if small_index > large_index:
            return [large_index, small_index]
        elif small_index == large_index:
            nums[small_index] += 1
            return [small_index, nums.index(sorted_nums[small])]
        else:
            return [small_index, large_index]
        