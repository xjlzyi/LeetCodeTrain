#编写一个函数来查找字符串数组中的最长公共前缀。
#如果不存在公共前缀，返回空字符串 ""。
# 输入: ["flower","flow","flight"]
# 输出: "fl"

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return result
        elif len(strs[0]) == 0:
            return result
        elif len(strs) == 1:
            return strs[0]
        #根据长短排序，最短的排在前面
        sort_strs = sorted(strs, key=len)
        for i in range(len(sort_strs[0])):
            if sort_strs[-1][i] != sort_strs[0][i]:
                return result
            result += sort_strs[0][i]
        return result
        

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))