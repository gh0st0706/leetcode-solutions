class Solution(object):
    def evaluate(self, s, knowledge):

        lookup = {}

        for key, value in knowledge:
            lookup[key] = value

        result = []
        i = 0

        while i < len(s):

            if s[i] == "(":
                j = i + 1

                while s[j] != ")":
                    j += 1

                key = s[i + 1:j]

                if key in lookup:
                    result.append(lookup[key])
                else:
                    result.append("?")

                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return "".join(result)