class Solution(object):
    def maxPalindromes(self, s, k):
      
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -=1

            return True 

        i = 0
        count = 0
        n = len(s)

        while i < n:

            if i + k <= n and is_palindrome(i, i+k - 1):
                count += 1
                i += k
            elif i + k +1 <= n and is_palindrome(i, i+ k):
                count += 1
                i += k + 1

            else :
                i += 1
        return count