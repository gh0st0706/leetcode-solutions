class Solution(object):
    def reverseDegree(self, s):
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        total = 0

        for i in range (len(s)):
            character = s[i]
            position = i + 1
            reversedValue = 26 - alphabet.index(character)

            score = reversedValue * position 

            total += score

        return total 


        
        