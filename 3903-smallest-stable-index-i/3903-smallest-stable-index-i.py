class Solution(object):
    def firstStableIndex(self, nums, k):
        if not nums:
            return -1


        n = len(nums)

        suffix_min = [0] * n

        suffix_min[n -1] = nums[n -1]

        for i in range(n -2, -1, -1):
         suffix_min[i] = min(nums[i], suffix_min[i +1])


        left_max = nums[0]

        for i in range(n):
            left_max = max(left_max, nums[i])

            score = left_max - suffix_min[i]

            if score <= k:
                return i 

        return -1

        