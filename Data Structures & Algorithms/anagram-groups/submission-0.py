class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        groups = {}

#first, check if they have the same letters, then move them to separate lists.

        for word in strs:
            key = ''.join(sorted(word))
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())