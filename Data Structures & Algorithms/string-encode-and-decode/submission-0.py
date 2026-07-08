class Solution:

    def encode(self, strs: List[str]) -> str:
        # Convert list into:
        # (Length of String)//SEPARATOR//"String" + ... 
        separator = "#"
        newstrs = []

        for i in strs: # loop through array
            length = len(i)
            newstrs.append(str(length))
            newstrs.append(separator)
            newstrs.append(i)
        
        encodedstr = ''.join(newstrs)

        return encodedstr



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i] 
                i += 1
            
            i += 1 #skip #

            strlen = int(length) #convert to int

            word = s[i:i + strlen]
            result.append(word)

            # move past the word

            i += strlen

        return result
