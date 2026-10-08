class Solution:
    def removeInvalidParentheses(self, s):

        def isValid(string):
            count = 0

            for ch in string:
                if ch == "(":
                    count += 1

                elif ch == ")":
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        current = {s}

        while True:
            result = []

            for string in current:
                if isValid(string):
                    result.append(string)

            if result:
                return result

            next_level = set()

            for string in current:
                for i in range(len(string)):
                    if string[i] == "(" or string[i] == ")":
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            current = next_level