# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_end = 0
        nex_end = 0
        step = 0
        
        i = 0
        while cur_end < n - 1 and i < n:
            # 获取下一次可跳跃的最大值
            nex_end = max(i + nums[i], nex_end)
            if i == cur_end:
                cur_end = nex_end
                step += 1
            i += 1
        
        return step
    
    def jump2(self, nums):
        if len(nums) < 2:
            return len(nums) - 1
        
        step = 1
        curr = prev = nums[0]
        for i in range(1, len(nums)):
            if i > curr:
                step += 1
                curr = prev
            prev = max(prev, i + nums[i])

        return step

if __name__ == "__main__":
    # nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))
    print(Solution().jump2(nums))
