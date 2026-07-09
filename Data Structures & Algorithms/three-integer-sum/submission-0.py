class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #numbers must be different index, must sum to 0.
        #fix one number, use two pointers... so sort

        sortednums = sorted(nums)
        result = []

        for i in range(len(sortednums)):
            #skip duplicate i
            if i > 0 and sortednums[i] == sortednums[i-1]:
                continue

            L_index = i + 1
            R_index = len(sortednums) - 1

            while L_index < R_index:
                total = sortednums[L_index] + sortednums[i] + sortednums[R_index]

                if total == 0: 
                    result.append([sortednums[i], sortednums[L_index], sortednums[R_index]])     

                    L_index += 1     
                    R_index -= 1
                    while L_index < R_index and sortednums[L_index] == sortednums[L_index - 1]:
                        L_index += 1

                elif total < 0:
                    L_index += 1
                else:
                    R_index -= 1


        return result