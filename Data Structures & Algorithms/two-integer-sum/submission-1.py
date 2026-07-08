class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums): 
            other = target - num
            if other in nums[i+1:]:
                j = nums[i+1:].index(other) + i + 1
                return [i,j]
        return -1
