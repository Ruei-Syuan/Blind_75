# # Intuition
# 陣列中不可相鄰取值

# # Approach
# 經典的 動態規劃 (Dynamic Programming, DP) 題型，常見於「House Robber」或「最大非相鄰子序列和」問題
# 核心思想是：在一個陣列中挑選元素，使得挑選的元素之間不能相鄰，並且最大化總和。

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [法1] DP切割
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 初始化 DP 陣列
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # DP: 上一個位置的最大值最大 OR 新的位置跳過一個往前取最大值的加總
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

        # [法2] 錯誤，在[2,1,1,2]=4, 會誤算 3 
        # sum_odd = 0
        # sum_even = 0
        # for i, val in enumerate(nums):
        #     if i % 2 == 1:
        #         sum_odd += val
        #     else:
        #         sum_even += val
        
        # return max(sum_odd, sum_even)

ss = Solution()
print(ss.rob([2,1,1,2])) # 4