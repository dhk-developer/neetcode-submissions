class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #regardless of array order, or if elements are consecutive in array
        #if there is any element that exists anywhere in the list, that is exactly 1 greater than previous element, then add 1 to consecutive counter.


        #naive approach would be to check for each element if there is any elemenet +1 in value from it, then repeat for all elements.

        #slightly better might be to do the same ^ but skip checking on any elements that are not the consecutive number. 

        #Put all numbers into a set... lookup is O(1).
        # Identify numbers that 'start a sequence' - we could define this as any number in the set where num-1 does not already exist in the set.

        numberset = set(nums)
        longest = 0

        for number in numberset:
            if number - 1 not in numberset:
                length = 1
                current = number

                while current + 1 in numberset:
                    length += 1
                    current += 1

                longest = max (longest, length) # check for each starting number

        return longest

