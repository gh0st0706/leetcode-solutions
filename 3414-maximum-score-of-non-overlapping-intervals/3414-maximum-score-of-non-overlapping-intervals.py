class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        arr = []

        # Keep original index
        for i in range(len(intervals)):
            l = intervals[i][0]
            r = intervals[i][1]
            w = intervals[i][2]

            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        n = len(arr)

        starts = []

        for i in range(n):
            starts.append(arr[i][0])

        # dp[i][k] stores:
        # (best score, chosen indices)
        dp = [[(0, ()) for k in range(5)] for i in range(n + 1)]

        for i in range(n - 1, -1, -1):

            l, r, w, original_index = arr[i]

            # -----------------------
            # Manual binary search
            # Find first start > r
            # -----------------------

            low = 0
            high = n

            while low < high:
                mid = (low + high) // 2

                if starts[mid] <= r:
                    low = mid + 1
                else:
                    high = mid

            next_i = low

            # -----------------------
            # Dynamic Programming
            # -----------------------

            for k in range(1, 5):

                # Skip this interval
                skip_score = dp[i + 1][k][0]
                skip_indices = dp[i + 1][k][1]

                # Take this interval
                take_score = w + dp[next_i][k - 1][0]

                take_indices = (original_index,) + dp[next_i][k - 1][1]
                take_indices = tuple(sorted(take_indices))

                # Pick better answer
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif skip_score > take_score:
                    dp[i][k] = (skip_score, skip_indices)

                else:
                    dp[i][k] = (
                        take_score,
                        min(take_indices, skip_indices)
                    )

        return list(dp[0][4][1])
        