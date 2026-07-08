class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        uniquenum = set(nums)
        

        for i in uniquenum:
            counter[i] = 0
            for j in nums:
                if i == j:
                    counter[i] += 1
        
        return [key for key, value in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]]