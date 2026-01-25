# # Intuition
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# # Approach
# 解法: A XOR B -> 
# REF: 
# https://medium.com/@smalldragon89/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98-371-sum-of-two-integers-368a8977fd68
# 陷阱:
# - 你遇到的 TLE 是因為 Python 整數無限精度，導致位運算加法模擬在某些情況下無法收斂。
# - 解法是：要嘛直接用 a+b，要嘛強制限制在 32-bit 範圍。
# 🎯 為什麼叫「補數」
# - 一補數 (One’s Complement)：把所有位元取反。
# - 二補數 (Two’s Complement)：在一補數的基礎上再加 1。

# # Complexity
# - Time complexity:O(1)
# - Space complexity:O(1)

# language: Python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 十六進位0xFFFFFFFF / 二進位(32個1) / 用 & MASK 可以把多餘的高位截掉，模擬「32 位整數溢位」
        MASK = 0xFFFFFFFF 
        # 32 位有號整數的最大值 / 十六進位 0x7FFFFFFF = 二進位 01111111111111111111111111111111
        MAX_INT = 0x7FFFFFFF

        # return a+b
        while b != 0:
            # 找出哪些位需要進位
            carry = (a & b) & MASK
            # 二進制相加但不考慮進位
            a = (a ^ b) & MASK
            # 把進位加到下一位
            b = (carry << 1) & MASK

        # - ~(a ^ MASK) / 把超過範圍的結果轉換成負數，模擬 32-bit 補數。
        return a if a <= MAX_INT else ~(a ^ MASK)
    
# 測試
print(Solution().getSum(5, 3))   # 輸出 8
# print(Solution().getSum(10, 25))# 輸出 35