#罗马数字转整数
#Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                sum = sum - d[s[i]]
            else:
                sum = sum + d[s[i]]
        return sum + d[s[-1]]
        
def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            s = next(lines)
            ret = Solution().romanToInt(s.upper())
            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
