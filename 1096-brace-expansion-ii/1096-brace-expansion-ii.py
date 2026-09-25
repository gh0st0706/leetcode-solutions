class Solution(object):
    def braceExpansionII(self, expression):

        def parse(i):
            current = {""}
            result = set()

            while i < len(expression):

                if expression[i].isalpha():
                    next_part = {expression[i]}
                    i += 1

                elif expression[i] == "{":
                    i += 1
                    next_part, i = parse(i)

                elif expression[i] == ",":
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                elif expression[i] == "}":
                    i += 1
                    result.update(current)
                    return result, i

                new_current = set()

                for word1 in current:
                    for word2 in next_part:
                        new_current.add(word1 + word2)

                current = new_current

            result.update(current)
            return result, i

        answer, i = parse(0)

        return sorted(answer)