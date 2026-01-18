# # Intuition
# 輸入 - 算看看哪天開始買進股票, 哪天賣出後, 會賺到做多錢, 請輸出最後賺的錢

# # Approach
# 將右邊list中最小 - 自己 = 得出賺錢的最大值

# # Complexity
# - Time complexity:
# - Space complexity:

# 【法一】
# - 每次迴圈都呼叫 max(prices[i:])
# - prices[i:] 是一個 切片 (slice)，會建立一個新的 list，長度大約是 n-i
# - max() 再去掃描這個新 list，時間複雜度是 O(n-i)
# - 整個迴圈跑下來，總時間複雜度是 O(n^2)
# 👉 當 prices 很大（例如 10^5），就會超時

# language: Python3
# class Solution1:
#     def maxProfit(self, prices: []) -> int:
#         profit = 0
#         for i, value in enumerate(prices):
#             gap = max(prices[i:]) - value 
#             # print (prices[i:])
#             # print (value)
#             # print (gap)

#             if gap > profit: 
#                 profit = gap     
            
#         return profit

# 【法二】
# - 只用一個變數 min_price 來追蹤目前最低股價
# - 每次迴圈只做 常數時間 O(1) 的比較與更新
# - 整個迴圈跑一次就結束，時間複雜度是 O(n)
# - 空間複雜度也是 O(1)，不需要額外切片或暫存陣列
# 你的程式在邏輯上是正確的，但因為每次都重新計算「後面最大值」，導致時間複雜度太高。
# 我的程式則是用 一次遍歷 + 追蹤最小值 的方式，把複雜度降到 O(n)，因此能避免 TLE。

class Solution:
    def maxProfit(self, prices: []) -> int:
        max_profit = 0
        min_price = float('inf')  # 初始值：無窮大

        for price in prices: 
            # 如果我跟過去比是最低價 (買入day), 更新最小值
            if price < min_price:
                min_price = price
            # 如果我扣掉過去最低價的profit是最大 (賣出day), 更新最大值
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

ss = Solution()
prices = [886,729,539,474]
print(ss.maxProfit(prices))