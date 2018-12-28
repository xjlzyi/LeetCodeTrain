"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_ = len(needle)
        if not len_:
            return 0
        else:
            for x in range(len_, len(haystack) + 1):
                if haystack[x-len_:x] == needle:
                    return x-len_
            return -1