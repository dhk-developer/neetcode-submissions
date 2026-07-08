class Solution:
    def isPalindrome(self, s: str) -> bool:
        #read string forward, read string backward
        #if forward = backwards, return true

        #ignore case sensitivity and non-alphanumeric characters

        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        back_s = cleaned[::-1] #start,stop,step

        if cleaned == back_s:
            return True

        else:
            return False