# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 当行数为1或大于字符串长度时，直接返回
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ['' for i in range(numRows)]
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow] += c
            # 当到达最上面或最下面一行时，转换方向
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        
        ret = ""
        for row in rows:
            ret += row
        return ret

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(Solution().convert(s, 3))