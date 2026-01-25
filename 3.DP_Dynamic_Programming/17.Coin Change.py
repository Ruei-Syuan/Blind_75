# # Intuition
# 輸入你可以換的硬幣種類 & 你所需要的總金額
# 輸出你最少需要幾枚硬幣，若都沒有輸出 0

# # Approach
# 最少硬幣湊金額
# 類似題目：完全背包問題（每個硬幣可以用無限次）
# - 定義 dp[i] = 湊成金額 i 所需的最少硬幣數。
# - 初始：dp[0] = 0（湊成 0 不需要硬幣）。
# dp[i]=min (dp[i-coin]+1)
# { 
# for coin in coins  
# if i - coin >= 0
# }- 
# 最後答案是 dp[amount]，如果仍是無限大，回傳 -1

# # Complexity
# - Time complexity:O(amount × coins)
# - Space complexity:O(amount)

# language: Python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 🧠 小技巧補充
        # - 最小值問題 → 用 inf 起手
        # 這樣每次 min() 都能更新成更小的答案。
        # - 最大值問題 → 用 -inf 起手
        # 這樣每次 max() 都能更新成更大的答案。
        # - 狀態可達問題 → 用布林值陣列
        # 例如 dp[i] = True 表示金額 i 可被湊出
        # x = float('inf')   # 正無限大
        # y = float('-inf')  # 負無限大
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
    