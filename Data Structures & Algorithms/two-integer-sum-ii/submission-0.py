class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #target - number, then find corresponding number if exists in list
        # share 1-indexed array.

        #continue through list until find a valid solution.

        for i in range(len(numbers)):
            num = numbers[i]
            find = target - num

            for j in range(i+1, len(numbers)):
                if numbers[j] == find:
                    return [i+1, j+1]


            