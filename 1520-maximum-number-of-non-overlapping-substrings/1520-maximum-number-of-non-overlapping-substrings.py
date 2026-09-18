class Solution(object):
    def maxNumOfSubstrings(self, s):
        first = {}
        last ={}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
                last[ch] = i
            
            last[ch] = i

        def get_end(start):
            end = last[s[start]]
            i = start

            while i<= end:
                ch = s[i]

                if first[ch] < start:
                    return -  1
                    

                end = max(end, last[ch])

                i += 1
            
            return end

        answer = []
        previous_end = -1

        for i in range(len(s)):

            if i != first[s[i]]:
                continue
            end = get_end(i)

            if end == -1:
                continue
            if i > previous_end:
                answer.append(s[i:end + 1])

            else:
                answer[-1] = s[i:end +1]

            previous_end = end

        return answer        