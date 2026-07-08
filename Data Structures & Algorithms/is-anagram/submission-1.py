class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for ch in s:
            anagram[ch] = anagram.get(ch, 0) + 1
        for ch in t:
            if ch not in anagram:
                return False
            anagram[ch] -= 1
            if anagram[ch] == 0:
                del anagram[ch]

        return not anagram
        