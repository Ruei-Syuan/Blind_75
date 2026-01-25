# # Intuition
# 輸入n, 一次可以爬1步or2步，請問有幾種方式可以達成

# # Approach
# DP，費波那契數列

# # Complexity
# - Time complexity:O(n)
# - Space complexity:O(n)

# language: Python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法 1：遞迴 + 記憶化
        # memo = {}
        # def f(k):
        #     if k <= 2:
        #         return k
        #     if k not in memo:
        #         memo[k] = f(k-1) + f(k-2)
        #     return memo[k]
        # return f(n)

        # 方法 2：動態規劃 (DP)
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # 方法 3：空間優化 (只存兩個變數)
        # if n <= 2:
        #     return n
        # a, b = 1, 2
        # for _ in range(3, n+1):
        #     a, b = b, a+b
        # return b