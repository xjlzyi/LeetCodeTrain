# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        elif n == 3:
            return sum(nums)

        nums.sort()
        res = 2**31
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                tmpSum = nums[i] + nums[l] + nums[r]
                if tmpSum == target:
                    return target
                elif abs(tmpSum - target) < abs(res - target):
                    res = tmpSum
                if tmpSum > target:
                    r -= 1
                else:
                    l += 1
                    
        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    print(Solution().threeSumClosest(nums, 1))
