class Solution(object):
    def resultArray(self, nums, k):
        dp = [0] * k
        result = [0] * k

        for num in nums:
            newDP = [0] * k

            newDP[num % k] += 1

           
            for r in range(k):
                newRemainder = (r * num) % k
                newDP[newRemainder] += dp[r]

            
            for r in range(k):
                result[r] += newDP[r]

            dp = newDP

        return result