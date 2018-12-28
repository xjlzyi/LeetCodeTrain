"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        #二分法查找
        while True:
            if j < 0:
                return 0
            if i >= j:
                return i + 1 if nums[i] < target else i
            
            mid = int((i + j) / 2)
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1