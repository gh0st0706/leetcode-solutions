class Solution(object):
    def missingMultiple(self, nums, k):
        nums = set(nums)

        n = k

        while n in nums:
            n += k
        
        return n
        
        
        