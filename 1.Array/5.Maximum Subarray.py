# # Intuition
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# # Approach
# 解法: (1)Kadane Algorithm (2)DP <最左/最右/中間 遞迴>
# https://hackmd.io/@asdfghjklll123/S1_lQtH5q

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(1)

# language: Python

# CODE
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        cur_end = nums[0]
        max_end = nums[0]
        
        for i in range(1, n):
            # 如果 nums[i] 本身比較大，就直接從 nums[i] 重新開始。
            cur_end = max(nums[i], cur_end + nums[i]) #判斷相加之後誰更大，當作結束點
            max_end = max(max_end, cur_end) #跟前幾個sub array加總結果相比，保留最大值
        
        return max_end 
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))  # 輸出 6