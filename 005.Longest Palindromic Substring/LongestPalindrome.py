# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 2:
            return s
        res = ''
        for i in range(len(s)):
            # check type 'aba'
            tmp = self.expandAroundCenter(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # check type 'abba'
            tmp = self.expandAroundCenter(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]