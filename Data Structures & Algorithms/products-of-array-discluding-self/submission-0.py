class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for each number in nums, multiply every other number except the current number.
        # could keep running track of numbers already looped through in separate list. 
        # in this case, prefix = 1, multiply number in nums by all future numbers, multiply by prefix, then add to prefix.

        result = [1] * len(nums) # makes [1, 1, 1 ... len(nums)]
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # multiply by everything past the current index
        suffix = 1

        for i in range(len(nums)-1, -1, -1):  #range(start,stop,step)
            result[i] *= suffix
            suffix *= nums[i]

        return result

        