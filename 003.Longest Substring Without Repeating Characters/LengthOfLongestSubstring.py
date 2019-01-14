# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or not len(s):
            return 0
        maxLen = 0
        curStr = ''
        for char in s:
            if char not in curStr:
                curStr += char
                curLen = len(curStr)
                if curLen > maxLen:
                    maxLen = curLen
            else:
            	# 从重复字节后面开始算
                curStr = curStr[curStr.index(char) + 1:] + char
        return maxLen