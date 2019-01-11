# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        result = 0
        while i < j:
            h = min(height[i], height[j])
            result = max(result, (j - i) * h)
            # 因为长度不断缩减，所以高度一定要大于之前一个值才能使面积更大
            while height[i] <= h and i < j: i += 1
            while height[j] <= h and i < j: j -= 1
        return result