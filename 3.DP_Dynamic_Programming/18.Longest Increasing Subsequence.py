# # Intuition
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# 輸入一個陣列，輸出此陣列中可以可遞增的子字串最長是多少

# # Approach
# DP
# REF:
# https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/leetcode-%E8%A7%A3%E9%A1%8C%E7%B4%80%E9%8C%84-300-longest-increasing-subsequence-f160358db4d1

# # Complexity
# - Time complexity:O(n^2)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n # 初始化 dp 陣列，每個位置的值為 1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # 檢查是否可以形成遞增子序列 
                    dp[i] = max(dp[i], dp[j] + 1) # // 更新 dp[i] 值
        
        return max(dp) # 返回 dp 陣列中的最大值