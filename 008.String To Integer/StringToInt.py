# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, 
#  or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:
# Input: "42"
# Output: 42

# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

class Solution(object):
    def __init__(self):
        self.INT_MIN = -2**31
        self.INT_MAX = 2**31-1

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        if len(str) <= 0: return 0
        # 去除前面的空格
        while index < len(str) and str[index] == ' ': index += 1
        if index >= len(str): return 0
        
        neg = 1
        if str[index] == '-' or str[index] == '+':
            neg = -1 if str[index] == '-' else 1
            index += 1

        ret = 0
        for i in range(index, len(str)):
            s = str[i]
            if s >= '0' and s <= '9':
                ret = ret * 10 + ord(s) - ord('0')
                tmp = ret * neg
                if tmp >= self.INT_MAX: 
                    return self.INT_MAX
                elif tmp <= self.INT_MIN: 
                    return self.INT_MIN 
            else: 
                break

        return ret * neg
    
    def myAtoiByRegex(self, str):
        import re
        match = re.search(r"^ *[-+]?[0-9]+", str)
        if match:
            match = int(match.group())
            if match < -2**31:
                return -2**31
            elif match > 2**31-1:
                return 2**31-1
            return match

if __name__ == "__main__":
    str = " +923 as"
    print(Solution().myAtoi(str))
    print(Solution().myAtoiByRegex(str))
