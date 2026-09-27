class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        current = ""

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(current)
                current = ""

            elif s[i] == ")":
                current = current[::-1]
                current = stack.pop() + current

            else:
                current += s[i]

        return current 


                

                

                





            

    

        