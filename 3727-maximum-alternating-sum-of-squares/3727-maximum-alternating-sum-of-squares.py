class Solution(object):
    def maxAlternatingSum(self, nums):

        def square(x):
            return x * x

        nums.sort(key=square)
        ans = 0

        for i in range(len(nums)):
            if i < len(nums) // 2:
                ans -= nums[i] ** 2
            else:
                ans += nums[i] ** 2

        return ans       
        