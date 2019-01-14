# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        elif n == 3:
            return [nums] if sum(nums) == 0 else []

        tnums = sorted(nums)
        result = []
        for i in range(n-2):
            if i > 0 and tnums[i] == tnums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                nsum = tnums[i] + tnums[l] + tnums[r]
                if nsum < 0:
                    l += 1
                elif nsum > 0:
                    r -= 1
                else:
                    result.append([tnums[i], tnums[l], tnums[r]])
                    while l + 1 < r and tnums[l] == tnums[l + 1]:
                        l += 1
                    while l < r - 1 and tnums[r] == tnums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result

    def threeSum2(self, nums):
        nums.sort()
        res = set()
        for i,a in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            d = {}
            for j, b in enumerate(nums[i + 1:]):
                if -a - b in d:
                    triple = sorted([a, b, -a - b])
                    res.add(tuple(triple))
                else:
                    d[b] = 1
        return list(res)

if __name__ == "__main__":
    nums = [-1, 0, 1, 1, -5, 2, 3, -4, -1]
    print(Solution().threeSum(nums))
    print(Solution().threeSum2(nums))
