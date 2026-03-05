# # Intuition
# 輸入 m*n 的棋盤大小，輸出從此棋盤左上角到右下角的 總步數

# # Approach
# [法一] 排列組合 (此題屬於 組合 DDRR, 排列會把 D 分成 D1 D2)
# [法二] DP，此步驟 = 左邊 + 上面
# - DP 是「一步一步累積」的邏輯，像在算路徑表格。
# - 排列組合 是「直接公式」的邏輯，像在算步數的分配。
# - 如果網格很單純 → 用組合公式最快。
# - 如果網格有障礙物或特殊規則 → 必須用 DP

# # Complexity
# - Time complexity:O(M+N)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def factorial(self, n):
        # 計算 n! 階乘
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # [法一] DP法
        # 建立 m x n 的表格，初始值都設為 1
        # dp = [[1] * n for _ in range(m)]
        # # 從第二行、第二列開始填表
        # for i in range(1, m):
        #     for j in range(1, n):
        #         # 每個格子的路徑數 = 上方 + 左方
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return dp[m-1][n-1]
        
        # [法二] 組合法
        totalSteps = (m - 1) + (n - 1)   # 總步數
        downSteps  = (m - 1)             # 向下的步數
            
        # 組合公式 C(totalSteps, downSteps) = totalSteps! / (downSteps! * (totalSteps - downSteps)!)
        return factorial(totalSteps) // (factorial(downSteps) * factorial(totalSteps - downSteps))

# print(uniquePathsDP(3, 7))  # 輸出: 28
        