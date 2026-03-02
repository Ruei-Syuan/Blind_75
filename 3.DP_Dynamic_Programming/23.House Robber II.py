# # Intuition
# 陣列中不可相鄰取值

# # Approach
# 經典的 動態規劃 (Dynamic Programming, DP) 題型，常見於「House Robber」或「最大非相鄰子序列和」問題
# 核心思想是：在一個陣列中挑選元素，使得挑選的元素之間不能相鄰，並且最大化總和。
# 頭、尾不可以同時選擇，所以解法只有選頭 or 選尾，兩者取最大

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def findMax(self, nums):
        # 初始化 DP 陣列
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # DP: 上一個位置的最大值最大 OR 新的位置跳過一個往前取最大值的加總
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP切割: 在圓形排列中，第一間房子和最後一間房子不能同時選。
        # 因此我們可以把問題拆成兩種情況：
        # - 不選第一間房子 → 在 nums[1:] 上做線性 DP。
        # - 不選最後一間房子 → 在 nums[:-1] 上做線性 DP。
        val1 = self.findMax(nums[1:])
        val2 = self.findMax(nums[:-1])

        return max(val1, val2)

ss = Solution()
print(ss.rob([1,2,3,1])) #[1,2,3]))