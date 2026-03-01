# # Intuition
# 輸入數列 & 加總目標, 輸出方法數

# # Approach
# DP- 回溯法（Backtracking）
# 思路: 利用 DP，每次答案等於上一次解法+1的邏輯
        
# # Complexity
# - Time complexity:O(log n)
# - Space complexity:O(log n)

# language: Python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # init
        dp = [0]*(target+1)
        dp[0] = 1 # 第一層一定只有 1 種方法

        # 思路: 利用 DP，每次扣一的解法+1
        # 計算組合
        # for n in nums:
        #     for i in range(n, target + 1):
        #         dp[i] += dp[i-n]

        # 排序 
        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]

        return dp[target]
                
ss = Solution()
print(ss.combinationSum4([1,2,3], 4))