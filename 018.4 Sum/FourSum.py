# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:
# The solution set must not contain duplicate quadruplets.

# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        elif n == 4:
            return [nums] if sum(nums) == target else []

        nums.sort()
        result = set()
        for i in range(n - 3):
            for j in range(i+1, n - 2):
                l = j + 1
                r = n - 1
                while l < r:
                    nsum = nums[i] + nums[j] + nums[l] + nums[r]
                    if nsum < target:
                        l += 1
                    elif nsum > target:
                        r -= 1
                    else:
                        result.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        while l + 1 < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l + 1 < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1

        return list(result)

    def fourSum2(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if N < 2 or len(nums) < N or nums[0] * N > target or nums[-1] * N < target:
                return

            if N == 2:
                l = 0
                r = len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNsum(nums[i + 1::], target - nums[i], N - 1, result + [nums[i]], results)
        results = []
        result = []
        findNsum(sorted(nums), target, 4, result, results)
        return results
       
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution().fourSum(nums, -1))
    print(Solution().fourSum2(nums, -1))
