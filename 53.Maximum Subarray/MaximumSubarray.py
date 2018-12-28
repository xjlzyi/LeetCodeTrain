"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_sum = 0
        num_max = -float("inf")
        for num in nums:
            num_sum += num
            if num_sum > num_max:
                num_max = num_sum
            #如果前面是负数，则重新开始计算
            if num_sum < 0:
                num_sum = 0
        return num_max