class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]
        prefix = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
            prefix[i][0] = i + 1

        for i in range(1, n):
            for j in range(1, k + 1):

                # Don't end a new segment at i
                dp[i][j] = dp[i - 1][j]

                # End a new segment at i
                dp[i][j] += prefix[i - 1][j - 1]

                dp[i][j] %= MOD

                # Update prefix sum
                prefix[i][j] = (
                    prefix[i - 1][j] + dp[i][j]
                ) % MOD

        return dp[n - 1][k]