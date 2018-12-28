# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        dic = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dic and dic[c] == l[-1]:
                l.pop()
            else:
                l.append(c)
        return len(l) == 0


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    
    lines = readlines()
    while True:
        try:
            s = next(lines)
            ret = Solution().isValid(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
