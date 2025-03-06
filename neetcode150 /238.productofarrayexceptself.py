class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1] * len(nums) 
        left[0] = 1
        for idx in range(1, len(nums)): 
            left[idx] = nums[idx - 1] * left[idx - 1]

        right = [1] * len(nums)
        right[len(nums) - 1] = 1
        # index from the back
        # python range is inclusive
        for idx in range(len(nums) - 2, -1, -1):
            right[idx] = nums[idx + 1] * right[idx + 1]

        # multiply both for result 
        result = [1] * len(nums)
        for idx in range(len(nums)): 
            result[idx] = left[idx] * right[idx]

        return result 
